from django.contrib import admin
from .models import Basket

# Register your models here.


class BasketAdmin(admin.ModelAdmin):
    list_display = ("user", "template", "quantity")
    list_filter = ("user", "template__category")


admin.site.register(Basket, BasketAdmin)