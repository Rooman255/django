from django.contrib import admin

from django.contrib import admin
from . import models


@admin.action(description="Обнулить")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(amount=0)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount']
    ordering = ['-amount']
    search_fields = ['description']
    search_help_text = 'description'
    actions = [reset_quantity]
    readonly_fields = ['added_at']
    fieldsets = [
        (
            None, {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Accounting',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Free information',
            {
                'description': 'Сводная информация',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'name'

    readonly_fields = ['reg_date']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'common_price']

    readonly_fields = ['date']
