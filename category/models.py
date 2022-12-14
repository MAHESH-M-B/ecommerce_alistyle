
from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=100, blank=True)
    cat_image = models.ImageField(upload_to='photos/category', blank=True)
    cat_location=models.TextField(max_length=100,blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        return reverse('product_by_category',args=[self.category_slug])

    def __str__(self):
        return self.category_name
