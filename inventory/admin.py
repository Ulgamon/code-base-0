from django.contrib import admin
from .models import Product, Brand, Category, Stock

class BrandAdmin(admin.ModelAdmin):
    model = Brand
    list_display = (
        "name",
        "brand_id",
    )

class StockAdmin(admin.ModelAdmin):
    model = Stock
    list_display = (
        "product",
        "units",
    )

admin.site.register(Product)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category)
admin.site.register(Stock, StockAdmin)
