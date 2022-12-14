from django.contrib import admin
from .models import Dish
# Register your models here.

class DishAdmin(admin.ModelAdmin):
    list_display=['name', 'type', 'price']
    list_filter=['price', 'type', 'name']
admin.site.register(Dish, DishAdmin)