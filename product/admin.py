from django.contrib import admin
from product.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price']
    prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Product,ProductAdmin)