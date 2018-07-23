from django.contrib import admin
from .models import Category, Product
# Register your models here.


# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','price', 'stock',]
    list_filter = ['name', 'price', 'stock',]
    list_editable = ['price', 'stock',]
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
