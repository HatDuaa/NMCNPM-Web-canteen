from django.contrib import admin
from .models import Dish
# Register your models here.

class DishAdmin(admin.ModelAdmin):
    list_display=['name', 'price']
    list_filter=['price', 'name']
admin.site.register(Dish, DishAdmin)