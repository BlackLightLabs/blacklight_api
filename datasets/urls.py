from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_datasets, name='datasets-list'),
    path('create/', views.create_dataset, name='dataset-create'),
    path('<int:dataset_id>/', views.get_dataset_detail, name='dataset-detail'),
    path('<int:dataset_id>/update/', views.update_dataset, name='dataset-update'),
    path('<int:dataset_id>/delete/', views.delete_dataset, name='dataset-delete'),
]
