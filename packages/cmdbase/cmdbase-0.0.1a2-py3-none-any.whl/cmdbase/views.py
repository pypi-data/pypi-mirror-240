from typing import Any
from django.db import models
from django.db.models import F, Value, Count
from django.views import generic
from django.urls import reverse
from django.conf import settings
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpRequest
from django.core.exceptions import PermissionDenied
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from django.db.models import QuerySet

from .commons import should_authenticate, can_search_items, filter_accessible_queryset
from .models import Category, Item, Issue, Report, ReportItem
from .categories import get_accessible_categories
from .displays import ItemDisplay
from .recents import add_recent, get_recents, clear_recents

from django.contrib.auth.mixins import UserPassesTestMixin



def get_accessible_items(request: HttpRequest) -> QuerySet[Item]:
    return filter_accessible_queryset(request, Item.objects)



class IsStaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class IndexView(generic.TemplateView):
    template_name = 'cmdbase/index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        search = self.request.GET.get('search', '')
        limit = int(self.request.GET.get('limit', '20'))
        context['search'] = search
        context['next_limit'] = limit * 2

        if search:
            if not can_search_items(self.request):
                raise PermissionDenied()
            
            results = search(search, limit=limit + 1)
            context["search_results"] = results[0:limit]
            context["search_results_more"] = len(results) > limit

        else: # not search
            if self.request.user.is_authenticated or not should_authenticate():
                context["recents"] = get_recents(self.request)
                context['categories'] = get_accessible_categories(self.request).annotate(items_count=Count('items')).order_by('name')
            
        return context


class AboutView(generic.TemplateView):
    template_name = 'cmdbase/about.html'


class ClearRecentView(generic.View):
    def get(self, request, *args, **kwargs):
        clear_recents(request)
        return HttpResponseRedirect(reverse('cmdbase:index'))


class SelectLanguageView(generic.View):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        redirect_to = self.request.POST.get('next', self.request.GET.get('next', reverse('cmdbase:index')))
        lang = self.request.POST.get('lang', self.request.GET.get('lang', None))
        response = HttpResponseRedirect(redirect_to)
        if lang:
            language_name = None
            for a_lang, a_name in settings.LANGUAGES:
                if a_lang == lang:
                    language_name = a_name
                    break 
            
            if language_name is not None:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
                messages.success(request, mark_safe(f"Language changed to <strong>{lang}</strong> ({language_name})."))
            else:
                messages.error(request, mark_safe(f"Unknown or unsupported language <strong>{lang}</strong>."))

        return response


class CategoryDetailView(generic.DetailView):
    template_name = 'cmdbase/category.html'

    def get_queryset(self):
        return get_accessible_categories(self.request).select_related('parent').prefetch_related('child_set')

    def get_object(self, queryset = None):
        if not self.request.user.is_authenticated and should_authenticate():
            raise PermissionDenied()

        obj = super().get_object(queryset)
        add_recent(self.request, obj)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve parents
        parents = []
        category = self.object.parent
        while category:
            parents.insert(0, category)
            category = category.parent
        context['parents'] = parents

        # Retrieve children
        me_and_children_id = [self.object.id]

        def recurse(category: Category):
            category.child_set.prefetch_related('child_set')
            for child in category.child_set.all():
                me_and_children_id.append(child.id)
                recurse(child)

        recurse(self.object)

        # Retrieve items
        context['items'] = Item.objects.filter(category_id__in=me_and_children_id).select_related('category')

        return context


class ItemDetailView(generic.DetailView):
    template_name = 'cmdbase/item.html'
    tab = None

    def get_queryset(self):
        return get_accessible_items(self.request).filter(category__slug=self.kwargs['category'])

    def get_object(self, queryset = None):
        if not self.request.user.is_authenticated and should_authenticate():
            raise PermissionDenied()
        
        obj = super().get_object(queryset)
        add_recent(self.request, obj)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item: Item = self.object
        
        context['tab'] = self.tab

        context['relations_count'] = item.targetrelation_set.count() + item.reverserelation_set.count()
                
        if self.tab == 'relations':
            relations = []

            for relation in item.targetrelation_set.select_related('target', 'target__category').all():
                relation.type = 'Target'
                relation.related = relation.target
                relations.append(relation)
            
            for relation in item.reverserelation_set.select_related('source', 'source__category').all():
                relation.type = 'Reverse'
                relation.related = relation.source
                relations.append(relation)

            context['relations'] = relations
        
        elif self.tab == 'reports':
            context['reportitems'] = item.reportitem_set.select_related('report').all()

        elif self.tab == 'properties':
            context['itemdisplay'] = ItemDisplay(item)

        return context


class ReportListView(IsStaffMixin, generic.TemplateView):
    template_name = 'cmdbase/report_list.html'


class ReportDetailView(IsStaffMixin, generic.DetailView):
    template_name = 'cmdbase/report.html'
    model = Report

    def get_context_data(self, **kwargs):
        self.object: Report
        context = super().get_context_data(**kwargs)
        context['root_reportitem'] = self.object.reportitem_set.filter(path__isnull=True).select_related('item', 'item__category').first()
        context['reportitem_set'] = self.object.reportitem_set.filter(item__isnull=False).select_related('item', 'item__category').all()
        context['reportissue_set'] = [self.ReportIssueDisplay(issue) for issue in self.object.issue_set.all()]
        return context
    
    class ReportIssueDisplay:
        def __init__(self, issue: Issue):
            self.display = issue.get_display()

            if issue.context and isinstance(issue.context, dict) and len(issue.context) == 2 and 'path' in issue.context and 'obj' in issue.context:
                self.path = issue.context['path']
                self.data = issue.context['obj']
            else:
                self.path = None
                self.data = issue.context


class ReporterDetailView(IsStaffMixin, generic.DetailView):
    template_name = 'cmdbase/reporter.html'
    model = get_user_model()


class IssueListView(IsStaffMixin, generic.TemplateView):
    template_name = 'cmdbase/issue_list.html'
