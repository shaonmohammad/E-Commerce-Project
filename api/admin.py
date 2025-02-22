from django.contrib import admin
from .models import Category,Product,Stock
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('id','name')
    search_fields = ('name',)

class StockInline(admin.TabularInline):  # or admin.StackedInline
    model = Stock
    extra = 1 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    inlines = [StockInline]
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')
    search_fields = ('product__name',)