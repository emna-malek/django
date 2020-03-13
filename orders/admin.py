from django.contrib import admin
from .models import OrderItem, order
from import_export.admin import ImportExportActionModelAdmin


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'email', 'city', 'postal_code',)
    list_filter = ('paid', 'created', 'updated',)
    search_fields = ['first_name', 'last_name', 'email']
    inlines = [
        OrderItemAdmin,
    ]


admin.site.register(order, OrderAdmin)
