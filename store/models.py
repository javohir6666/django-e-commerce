from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField(upload_to='uploads/category_photos/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, help_text="0=default ,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default ,1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500,null=False, blank=False)
    
    
    class Meta:
        verbose_name_plural = 'Categories'
        
        
    def __str__(self):
        return self.title
    
    