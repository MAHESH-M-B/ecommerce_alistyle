from django.db import models
from category.models import Category
# Create your models here.
class Store(models.Model):
    Product_name=models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    product_price=models.IntegerField()
    product_image=models.ImageField(upload_to='photos/products')
    product_description=models.TextField(max_length=100,blank=True)
    products_stock=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,models.CASCADE)


    


    
    def __str__(self):
        return self.Product_name
