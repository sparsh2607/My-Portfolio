from django.contrib import admin
from .models import Project
 
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'category')
