from django.contrib.admin import register
from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django.http import HttpRequest
from .models import Category, Item, Prop, IssueNature, Report, ReportItem, ReportOrigin

if getattr(settings, 'WITH_IMPORT_EXPORT', False):
    from import_export.admin import ImportExportModelAdmin as ModelAdmin
else:
    from django.contrib.admin import ModelAdmin


class AdminMixin:
    def set_text_blank_values_to_null(self, obj: models.Model):
        """
        Set blank values to null for text fields.
        """
        for field in obj._meta.fields:
            if isinstance(field, (models.TextField,models.CharField)) and field.blank and field.null:
                value = getattr(obj, field.attname, None)
                if value == '':
                    setattr(obj, field.attname, None)

    def save_model(self, request: HttpRequest, obj: models.Model, form: ModelForm, change: bool):
        self.set_text_blank_values_to_null(obj)
        super().save_model(request, obj, form, change)


@register(Category)
class CategoryAdmin(AdminMixin, ModelAdmin):
    list_display = ['name', 'parent']
    search_fields = ['name', 'slug']
    readonly_fields = ['slug', 'created', 'updated']
    fields = [
        ('name', 'slug'),
        'parent',
        'help',
        ('created', 'updated'),
    ]


@register(Prop)
class PropAdmin(AdminMixin, ModelAdmin):
    list_display = ['fullname', 'category', 'ordinal', 'nature', 'unit']
    list_filter = ['category', 'nature', 'unit']
    search_fields = ['fullname']
    readonly_fields = ['fullname', 'created', 'updated']
    fields = [
        'category',
        'name',
        ('parent', 'fullname'),
        'ordinal',
        ('nature', 'unit'),
        ('index', 'index_with', 'search'),
        'help',
        ('created', 'updated'),
    ]


@register(Item)
class ItemAdmin(AdminMixin, ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name', 'slug']
    readonly_fields = ['slug', 'created', 'created_by', 'updated', 'updated_by']
    fields = [
        'category',
        ('name', 'slug'),
        'data',
        ('created', 'created_by', 'updated', 'updated_by'),
    ]

    def save_model(self, request: HttpRequest, obj: Item, form: ModelForm, change: bool):
        self.set_text_blank_values_to_null(obj)

        data = {
            "_c": form.cleaned_data["category"].name,
            "name": form.cleaned_data["name"],
        }

        if kv := form.cleaned_data["data"]:
            for key, value in kv.items():
                data[key] = value

        report = Report.objects.create(by=request.user, origin=ReportOrigin.ADMIN)
        reportitem = report.reportitem_set.create(path=None, data=data)
        obj.save(reportitem=reportitem)
