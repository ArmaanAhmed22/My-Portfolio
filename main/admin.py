from django.contrib import admin
from django import forms
from .models import *
from django_json_widget.widgets import JSONEditorWidget
# Register your models here.
admin.site.register(SocialMedia)

class ProjectAdmin(admin.ModelAdmin):
    #fields = ['title', 'short_title', 'description', 'short_description', 'project_link', 'where_is_projects_on_website', 'list_tags']
    
    fieldsets = [
        ("Title", {"fields": ['title', 'short_title']}),
        ("Description", {"fields": ['description', 'short_description']}),
        ("Other", {"fields": ['project_link', 'where_is_projects_on_website', 'list_tags']}),
    ]

admin.site.register(Project, ProjectAdmin)

admin.site.register(ProjectTag)

admin.site.register(CVCategory)

class CVItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Category", {"fields": ["category"]}),
        ("Start Date", {"fields": ["start_month", "start_year"]}),
        ("End Date", {"fields": ["end_month", "end_year"]}),
        ("Content", {"fields": ["title"]})
    ]

admin.site.register(CVItem, CVItemAdmin)


DATA_SCHEMA = {
    'type': 'array',
    'title': 'expandible',
}

class JSONModelAdminForm(forms.ModelForm):
    class Meta:
        model = CVItemListExpandible
        fields = '__all__'
        widgets = {
            'data': JSONEditorWidget(DATA_SCHEMA),
        }

class CVItemListExpandibleAdmin(admin.ModelAdmin):
    form = JSONModelAdminForm

admin.site.register(CVItemListExpandible, CVItemListExpandibleAdmin)
