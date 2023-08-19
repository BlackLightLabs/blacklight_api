from django.urls import path
from . import views

urlpatterns = [
    path('analyses/', views.get_analyses, name='analyses-list'),
    path('analyses/create/', views.create_analysis, name='analysis-create'),
    path('analyses/<int:analysis_id>/', views.analysis_detail, name='analysis-detail'),
]
