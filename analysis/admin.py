from django.contrib import admin

from .models import Analysis

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'dataset', 'types', 'cost', 'completed']
    list_filter = ['types', 'completed']
    search_fields = ['user__username', 'dataset__dataset_name']

admin.site.register(Analysis, AnalysisAdmin)
