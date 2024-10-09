from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline

# Register your models here.
from .models import Quote, QuoteItems

class QuoteItemsInline(TabularInline):
    model = QuoteItems

@admin.register(Quote)
class QuoteAdmin(ModelAdmin):
    list_display = ['company', 'quote_total_price', 'status']
    search_fields = ['company','status']
    list_filter = ['status', 'company']
    inlines = [QuoteItemsInline]






