from django.contrib import admin
from .models import Page
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget

# Register your models here.
@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_filter = ['is_active', 'created_at']
    date_hierarchy = 'created_at'
    fieldsets = [
        (None, {
            'fields': ['title', 'slug', 'content']
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ['is_active']
        }),
    ]
    readonly_fields = ['created_at', 'last_update']
    list_per_page = 10
    actions = ['make_active', 'make_inactive']

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = 'Mark selected pages as active'

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = 'Mark selected pages as inactive'