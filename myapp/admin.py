from django.contrib import admin
from .models import ProductMst, ProductSubCat

@admin.register(ProductMst)
class ProductMstAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name')

@admin.register(ProductSubCat)
class ProductSubCatAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_model', 'product_price')
