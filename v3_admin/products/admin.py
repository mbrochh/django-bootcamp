from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price'] 
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    
    
admin.site.register(models.Product, ProductAdmin)