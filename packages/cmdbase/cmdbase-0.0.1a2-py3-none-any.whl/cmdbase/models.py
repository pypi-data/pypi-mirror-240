from __future__ import annotations
import logging
from typing import TYPE_CHECKING
from django.db import models
from django.db.models import Q, F, Count
from django.db.transaction import atomic
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils import timezone
from django.urls import reverse
from zut import choices_table, _UNSET, slugify
from cmdbase_utils.choices import ReportAction, ReportOrigin
from .bases import HistoryManager, ItemDataManager

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager

logger = logging.getLogger(__name__)

DEFAULT_MAXLEN = 255


class Category(models.Model):
    NAME_MAXLEN = 20
    ROOT_NAME = 'Item'

    name = models.CharField(max_length=NAME_MAXLEN, unique=True, validators=[RegexValidator(r'^[A-Z][a-zA-Z0-9]+$')])
    slug = models.SlugField(max_length=NAME_MAXLEN, unique=True)
    parent: Category = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True, related_name='child_set')
    help = models.CharField(max_length=DEFAULT_MAXLEN, null=True, blank=True)
    # ----------
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Relations
    child_set: RelatedManager[Category]
    ancestor_set: RelatedManager[CategoryAncestor]
    descendant_set: RelatedManager[CategoryAncestor]    
    directprop_set: RelatedManager[Prop]
    categoryprop_set: RelatedManager[CategoryProp]

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'
        constraints = [
            models.CheckConstraint(check=Q(parent__isnull=False)|Q(name='Item'), name="only_root_item_has_no_parent"), # 'Item' = Category.ROOT_NAME
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cmdbase:category', args=[self.slug])

    def save(self, **kwargs):
        self.slug = slugify(self.name)
        super().save(**kwargs)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='items')
    name = models.CharField(max_length=DEFAULT_MAXLEN)
    slug = models.SlugField(max_length=DEFAULT_MAXLEN)
    data = models.JSONField(null=True, blank=True, encoder=DjangoJSONEncoder)
    # ----------
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT, related_name='+')
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT, related_name='+')
    # ----------
    reportitem_set: RelatedManager[ReportItem]
    targetrelation_set: RelatedManager[Relation]
    reverserelation_set: RelatedManager[Relation]
    issue_set: RelatedManager[Issue] = GenericRelation('Issue', content_type_field='on_type', object_id_field='on_id', related_query_name='item')

    class Meta:
        unique_together = [
            ('category', 'name'),
            ('category', 'slug'),
        ]
        ordering = ['name', 'category']

    def __str__(self):
        return f"{self.name} ({self.category})"

    def get_absolute_url(self):
        return reverse('cmdbase:item', args=[self.category.slug, self.slug])
    
    def clean(self):
        if not isinstance(self.data, (type(None),dict)):
            raise ValidationError({'data': ValidationError("Data must be either a dictionnary or null, not %(typename)s.", params={'typename': type(self.data).__name__})})
        
        if self.data:
            for key in self.data:
                if not isinstance(key, str) or key in self.invalid_data_keys() or key.startswith('_'):
                    raise ValidationError({'data': ValidationError("Invalid key in data: %(name)s.", params={'name': key})})
                
        try:
            self.data, self._discovered_relations = self.data_manager.encode()
        except Exception as err:
            raise ValidationError({'data': err})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_manager = ItemDataManager(self)

    @atomic
    def save(self, *, reportitem: ReportItem, **kwargs):
        if reportitem.item:
            raise ValueError(f"reportitem's item should not be set before calling item.save() method")
        if reportitem.action:
            raise ValueError(f"reportitem's action should not be set before calling item.save() method")
        
        reportitem.item = self

        self.slug = slugify(self.name)

        if not hasattr(self, '_discovered_relations') or self._discovered_relations is None:
            # NOTE: if self._discovered_relations is not None, we consider data was already encoded (e.g. in clean method)
            self.data, self._discovered_relations = self.data_manager.encode()

        if not self.id:
            reportitem.action = ReportAction.CREATE
            self.created_by = reportitem.report.by
        else:
            reportitem.action = ReportAction.UPDATE
        self.updated_by = reportitem.report.by

        super().save(**kwargs)

        self.data_manager.update_relations(self._discovered_relations)
        self._discovered_relations = None

        reportitem.save()


    @classmethod
    def invalid_data_keys(cls):
        try:
            return cls._invalid_data_keys
        except:
            cls._invalid_data_keys = set([field.name for field in Item._meta.fields])
            for field in Item._meta.fields:
                if not field.attname in cls._invalid_data_keys:
                    cls._invalid_data_keys.add(field.attname)
            return cls._invalid_data_keys


@choices_table(app_label='cmdbase')
class PropNature(models.TextChoices):
    TEXT = 'T'
    INTEGER = 'I'
    DECIMAL = 'D'
    BOOLEAN = 'B'
    DATETIME = 'M' # M for Moment
    DATE = 'J' # J for Jour
    TIME = 'H' # H for Heure
    RELATION = 'R'
    SECTION = 'S'
    TABLE = 'A' # A for Array
    CHOICES = 'C' # Text or int choices


@choices_table(app_label='cmdbase')
class PropIndexConfig(models.TextChoices):
    DEFAULT = 'I' # Index
    UNIQUE = 'U'
    FOR_CATEGORY = 'C'


class Prop(models.Model):
    NAME_MAXLEN = 20
    UNIT_MAXLEN = 20
    DEFAULT_ORDINAL = 1000

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='directprop_set')
    parent: Prop = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True, related_name='child_set')
    name = models.CharField(max_length=NAME_MAXLEN, validators=[RegexValidator(r'^[a-z][a-z0-9_]+$')])
    fullname = models.CharField(max_length=DEFAULT_MAXLEN) # managed by trigger
    ordinal = models.SmallIntegerField(default=DEFAULT_ORDINAL)
    nature = models.CharField(max_length=1, choices=PropNature.choices, null=True, blank=True)
    unit = models.CharField(max_length=UNIT_MAXLEN, null=True, blank=True)
    index = models.CharField(max_length=10, null=True, blank=True) # see PropIndexConfig
    index_with = ArrayField(models.CharField(max_length=NAME_MAXLEN), null=True, blank=True)
    search = models.BooleanField(default=False)
    help = models.CharField(max_length=DEFAULT_MAXLEN, null=True, blank=True)
    # ----------
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Relations
    child_set: RelatedManager[Prop]

    class Meta:
        unique_together = [
            ('category', 'parent', 'name'),
            ('category', 'fullname'),
        ]
        ordering = ['fullname', 'category']

    def __str__(self):
        return f"{self.fullname} ({self.category})"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not hasattr(type(self), '_history'):
            type(self)._history = HistoryManager(type(self))
        self._history_snapshot = self._history.get_snapshot(self)
    
    @atomic
    def save(self, **kwargs):
        from .categories import update_prop_index
        
        super().save(**kwargs)
        self.refresh_from_db(fields=['fullname'])

        if self._history_snapshot['id']: # updated
            if self._history_snapshot['category_id'] != self.category_id or self._history_snapshot['fullname'] != self.fullname: # prop changed
                if prev := self.objects.filter(category_id=self._history_snapshot['category_id'], fullname=self._history_snapshot['fullname']).first():
                    update_prop_index(prev, prev.index, prev.index_with)

        update_prop_index(self, self.index, self.index_with)

    @atomic
    def delete(self, **kwargs):
        from .categories import update_prop_index       
        
        super().delete(**kwargs)

        update_prop_index(self, None)


class Relation(models.Model):
    """
    Automatically filled when Item instances are saved.

    NOTE: relations are kept Item data (and not only in this Relation model) so that:
    - Item's data remain the single source of trust (Relation model can be rebuilt from Item's data)
    - Relations can be part of unique indices
    """
    source = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='targetrelation_set')
    path = models.CharField(max_length=DEFAULT_MAXLEN)
    target = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reverserelation_set')

    class Meta:
        unique_together = [
            ('source', 'path'),
        ]


class Report(models.Model):
    at = models.DateTimeField(default=timezone.now, db_index=True)
    by = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    origin = models.CharField(max_length=1, choices=ReportOrigin.choices)
    # ----------
    created = models.DateTimeField(auto_now_add=True)
    # ----------
    reportitem_set: RelatedManager[ReportItem]
    issue_set: RelatedManager[Issue] = GenericRelation('Issue', content_type_field='on_type', object_id_field='on_id', related_query_name='report')

    class Meta:
        ordering = ['-at', '-id']

    class CustomManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().annotate(item_count=Count('reportitem_set', filter=Q(reportitem_set__item__isnull=False)), issue_count=Count('issue_set'))

    objects = CustomManager()

    def __str__(self):
        return f"Report #{self.pk}"
    
    def get_absolute_url(self):
        return reverse('cmdbase:report', args=[self.pk])
    

class ReportItem(models.Model):
    report = models.ForeignKey(Report, on_delete=models.RESTRICT, related_name='reportitem_set')
    item = models.ForeignKey(Item, on_delete=models.RESTRICT, null=True, blank=True) # may be null for root item (path = null) with issues
    action = models.CharField(max_length=1, choices=ReportAction.choices, null=True, blank=True)
    path = models.CharField(max_length=DEFAULT_MAXLEN, null=True, blank=True)
    data = models.JSONField(encoder=DjangoJSONEncoder)

    class Meta:
        ordering = ['report', 'id']
        constraints = [
            models.UniqueConstraint(fields=['report', 'item'], condition=Q(path__isnull=True), name="unique_report_root_item"),
            models.CheckConstraint(check=Q(item__isnull=False, action__isnull=False)|Q(path__isnull=True), name="item_and_action_required_if_not_root_path"),
        ]
    

class IssueNature(models.Model):
    value = models.CharField(max_length=DEFAULT_MAXLEN, unique=True)

    class Meta:
        ordering = ['value']

    def __str__(self):
        return self.value
    

class Issue(models.Model):
    nature = models.ForeignKey(IssueNature, on_delete=models.RESTRICT)
    nature_args = models.JSONField(encoder=DjangoJSONEncoder)
    # ----------
    on_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT)
    on_id = models.PositiveIntegerField()
    on = GenericForeignKey("on_type", "on_id")
    # ----------
    context = models.JSONField(encoder=DjangoJSONEncoder, null=True, blank=True)
    # ----------
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    acked = models.DateTimeField(null=True, blank=True)
    acked_by = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT, null=True, blank=True, related_name='+')

    class Meta:
        ordering = ['nature']
        unique_together = [
            ('nature', 'nature_args', 'on_type', 'on_id'),
        ]
        indexes = [
            models.Index(fields=['on_type', 'on_id']),
        ]

    def get_display(self):
        if isinstance(self.nature_args, dict):
            return self.nature.value.format(**self.nature_args)
        else:
            result = self.nature.value
            if isinstance(self.nature_args, list):
                result += ': ' + ', '.join(str(arg) for arg in self.nature_args)
            elif self.nature_args:
                result += f': {self.nature_args}'
            return result


# -----------------------------------------------------------------------------
# region Views

class CategoryAncestor(models.Model):
    descendant = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='ancestor_set')
    descendant_name = models.CharField(max_length=Category.NAME_MAXLEN)
    depth = models.SmallIntegerField()
    ancestor = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='descendant_set')
    ancestor_name = models.CharField(max_length=Category.NAME_MAXLEN)

    class Meta:
        managed = False
        ordering = ['descendant_name', '-depth']


class CategoryProp(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='categoryprop_set')
    category_name = models.CharField(max_length=Category.NAME_MAXLEN)
    prop = models.ForeignKey(Prop, on_delete=models.DO_NOTHING, related_name='+')
    prop_fullname = models.CharField(max_length=DEFAULT_MAXLEN)
    prop_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='+')
    prop_category_name = models.CharField(max_length=Category.NAME_MAXLEN)
    prop_name = models.CharField(max_length=Prop.NAME_MAXLEN)
    prop_parent = models.ForeignKey(Prop, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='+')
    prop_parent_name = models.CharField(max_length=Prop.NAME_MAXLEN, null=True, blank=True)
    prop_parent_fullname = models.CharField(max_length=Prop.NAME_MAXLEN, null=True, blank=True)
    prop_ordinal = models.SmallIntegerField(default=1000)
    prop_nature = models.CharField(max_length=1, choices=PropNature.choices, default=PropNature.TEXT)
    prop_unit = models.CharField(max_length=Prop.UNIT_MAXLEN, null=True, blank=True)
    prop_index = models.CharField(max_length=10, null=True, blank=True) # see PropIndexConfig
    prop_index_with = ArrayField(models.CharField(max_length=Prop.NAME_MAXLEN), null=True, blank=True)
    prop_search = models.BooleanField(default=False)
    prop_help = models.TextField(max_length=DEFAULT_MAXLEN, null=True, blank=True)

    class Meta:
        managed = False
        ordering = ['category_name', F("prop_parent_fullname").asc(nulls_first=True), 'prop_ordinal', 'prop_fullname']


class Report_Detail(models.Model):
    at = models.DateTimeField(default=timezone.now, db_index=True)
    by = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, related_name='+')
    origin = models.CharField(max_length=1, choices=ReportOrigin.choices)
    item_count = models.BigIntegerField()
    issue_count = models.BigIntegerField()
    root_reportitem = models.ForeignKey(ReportItem, on_delete=models.DO_NOTHING, null=True, blank=True)
    root_item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, null=True, blank=True)
    root_action = models.CharField(max_length=1, choices=ReportAction.choices, null=True, blank=True)
    root_data = models.JSONField(encoder=DjangoJSONEncoder, null=True, blank=True)
    # ----------
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        ordering = ['-at', '-id']

    def __str__(self):
        return f"Report #{self.pk}"
    
    def get_absolute_url(self):
        return reverse('cmdbase:report', args=[self.pk])
    

# endregion
