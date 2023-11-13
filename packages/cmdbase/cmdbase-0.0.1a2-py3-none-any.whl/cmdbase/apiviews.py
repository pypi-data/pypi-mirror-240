import logging
from rest_framework import permissions, generics, serializers, pagination
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django.db.models import Count
from django.contrib.auth.models import AbstractUser
from django_filters import rest_framework as filters
from .models import Issue, Item, Report, Report_Detail, ReportAction, ReportItem, ReportOrigin
from .commons import can_search_items, can_report_items
from .searches import search
from .reports import report_content

logger = logging.getLogger(__name__)
       

class SearchAPIView(APIView):
    class SearchPermission(permissions.BasePermission):
        def has_permission(self, request: Request, view):
            return can_search_items(request)
        
    permission_classes = [SearchPermission]

    def get(self, request: Request, *args, **kwargs):
        results = search(search=request.GET.get('search'), limit=self.request.GET.get('limit', 20))
        return Response(results)


class ReportAPIView(generics.ListAPIView):
    class ReportPermission(permissions.BasePermission):
        def has_permission(self, request: Request, view):
            if request.method == 'POST':
                return can_report_items(request)
            else:
                return request.user.is_staff
            
    
    class ReportSerializer(serializers.ModelSerializer):
        by_username = serializers.CharField(source='by.username')
        root_item_fullname = serializers.CharField(source='root_item.__str__', default=None)
        root_item_url = serializers.CharField(source='root_item.get_absolute_url', default=None)
        item_count = serializers.IntegerField()
        issue_count = serializers.IntegerField()

        class Meta:
            model = Report_Detail
            fields = ['id', 'at', 'by', 'by_username', 'origin', 'item_count', 'issue_count', 'root_item', 'root_item_fullname', 'root_item_url', 'root_action', 'root_data', 'created']
        

    class ReportFilter(filters.FilterSet):
        min_at = filters.DateTimeFilter(field_name='at', lookup_expr='gte')
        max_at = filters.DateTimeFilter(field_name='at', lookup_expr='lte')
        item_count = filters.Filter()
        issue_count = filters.Filter()

        class Meta:
            model = Report_Detail
            fields = ['by', 'origin', 'item_count', 'issue_count', 'root_item', 'root_action']


    permission_classes = [ReportPermission]
    queryset = Report_Detail.objects.select_related('root_item', 'root_item__category')
    serializer_class = ReportSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = ReportFilter
    pagination_class = pagination.LimitOffsetPagination
    ordering_fields = ['at', 'item_count', 'issue_count']
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    # GET: retrieve list of items
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # POST: report item(s)
    def post(self, request: Request, *args, **kwargs):
        by = request.user
        origin = ReportOrigin.API

        reports = report_content(request.data, by=by, origin=origin)

        summary = self.get_reports_summary(reports, by=by, origin=origin)

        return Response(summary)
        

    def get_reports_summary(self, reports: 'list[Report]', *, by: AbstractUser, origin: ReportOrigin):
        result = {
            'reports': 0,
            'by': by.pk,
            'by_username': by.username,
            'origin': origin,
            'items': 0,
            'created': 0,
            'updated': 0,
            'issues': 0,
            'root_items': [],
            'issue_details': [],
        }

        for report in reports:
            result['reports'] += 1            

            issues = []
            for ri in report.issue_set.all():
                result['issues'] += 1
                issues.append(ri.get_display())

            if issues:
                result['issue_details'].append(issues[0] if len(issues) == 1 else issues)
            else:
                result['issue_details'].append(None)

            root_reportitem: ReportItem = None
            for ri in report.reportitem_set.all():
                result['items'] += 1
                if not ri.path:
                    root_reportitem = ri
                if ri.action == ReportAction.CREATE:
                    result['created'] += 1
                elif ri.action == ReportAction.UPDATE:
                    result['updated'] += 1

            if root_reportitem and root_reportitem.item:
                result['root_items'].append({
                    "id": root_reportitem.item.id,
                    "fullname": str(root_reportitem.item),
                    "url": root_reportitem.item.get_absolute_url(),
                    "action": root_reportitem.action,
                })
            else:
                result['root_items'].append(None)

        return result


class IssueAPIView(generics.ListAPIView):
    class IssueSerializer(serializers.ModelSerializer):
        display = serializers.CharField(source='get_display')
        on_type_app_label = serializers.CharField(source='on_type.app_label')
        on_type_model = serializers.CharField(source='on_type.model')
        acked_by_username = serializers.CharField(source='acked_by.username', default=None)
        on = serializers.IntegerField(source='on_id')
        on_name = serializers.CharField(source='on.__str__')
        on_url = serializers.CharField(source='on.get_absolute_url')

        class Meta:
            model = Issue
            fields = ['id', 'display', 'on_type', 'on_type_app_label', 'on_type_model', 'on', 'on_name', 'on_url', 'context', 'created', 'updated', 'acked', 'acked_by', 'acked_by_username']


    permission_classes = [permissions.IsAdminUser]
    queryset = Issue.objects.get_queryset()
    serializer_class = IssueSerializer
    pagination_class = pagination.LimitOffsetPagination
    authentication_classes = [SessionAuthentication, TokenAuthentication]
