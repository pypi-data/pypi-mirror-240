from django.urls import path
from . import views
from . import apiviews

app_name = 'cmdbase'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('select-language/', views.SelectLanguageView.as_view(), name='select_language'),    
    path('clear-recent/', views.ClearRecentView.as_view(), name='clear_recent'),
    path('about/', views.AboutView.as_view(), name='about'),

    path('report/<int:pk>', views.ReportDetailView.as_view(), name='report'),
    path('report/', views.ReportListView.as_view(), name='report_list'),
    path('reporter/<int:pk>', views.ReporterDetailView.as_view(), name='reporter'),
    
    path('issue/', views.IssueListView.as_view(), name='issue_list'),

    path('-/<slug:category>/<slug:slug>/relation/', views.ItemDetailView.as_view(tab='relations'), name='item_relation_list'),
    path('-/<slug:category>/<slug:slug>/issue/', views.ItemDetailView.as_view(tab='issues'), name='item_issue_list'),
    path('-/<slug:category>/<slug:slug>/report/', views.ItemDetailView.as_view(tab='reports'), name='item_report_list'),
    path('-/<slug:category>/<slug:slug>/', views.ItemDetailView.as_view(tab='properties'), name='item'),
    path('-/<slug:slug>/', views.CategoryDetailView.as_view(), name='category'),

    path('api/search/', apiviews.SearchAPIView.as_view()),
    path('api/report/', apiviews.ReportAPIView.as_view(), name='api_report'),
    path('api/issue/', apiviews.IssueAPIView.as_view(), name='api_issue'),
]
