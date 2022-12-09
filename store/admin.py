from django.contrib import admin
from .models import Category, Product
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'slug')
    list_filter = ('status', 'trending')
    search_fields = ['title', 'meta_keywords']
admin.site.register(Category, AdminCategory)

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'slug', 'selling_price')
    list_filter = ('status', 'trending', 'selling_price')
    search_fields = ['title', 'meta_keywords', 'selling_price']
admin.site.register(Product, AdminProduct)