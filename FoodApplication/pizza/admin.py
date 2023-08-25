from django.contrib import admin
from . models import Pizza, Size

# Register your models here.

admin.site.register(Size)
# admin.site.register(Pizza)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['topping1', 'topping2', 'size']
    list_filter = ['size']
