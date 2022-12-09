from django.contrib import admin
from .models import Category
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'slug')
    list_filter = ('status', 'trending')
    search_fields = ['title', 'meta_keywords']
admin.site.register(Category, AdminCategory)