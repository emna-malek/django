from django.contrib import admin
from myapp.models import Posts
from myapp.models import Category
from myapp.models import Product
from django.contrib import admin

# Register your models here.
admin.site.register(Posts)


class CategoryAdmin(admin.ModelAdmin):
    # Admin view for category

    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    # Admin view for product

    list_display = ('name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated',)
    list_filter = ('available', 'created', 'updated', 'category',)
    list_editable = ('price', 'stock', 'available',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
