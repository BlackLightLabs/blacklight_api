from django.contrib import admin
from .models import Dataset

class DatasetAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'dataset_name', 'date_created', 'processed']
    list_filter = ['processed', 'date_created']
    search_fields = ['dataset_name', 'user__username']
    ordering = ['-date_created']

admin.site.register(Dataset, DatasetAdmin)

# Register your models here.
