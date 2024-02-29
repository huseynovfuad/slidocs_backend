from django.contrib import admin
from .models import Wishlist

# Register your models here.



class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user", "template")
    list_filter = ("template__category", )


admin.site.register(Wishlist, WishlistAdmin)