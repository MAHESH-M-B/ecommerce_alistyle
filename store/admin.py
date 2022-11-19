from django.contrib import admin
from .models import Store
class StoreAdmin(admin.ModelAdmin):
    list_display=('Product_name','product_price','products_stock','category','modified_date','is_available')
    prepopulated_fields={'slug':('Product_name',)}
# Register your models here.
admin.site.register(Store,StoreAdmin)