from django.contrib import admin
from .models import (
    Category, Template, TemplateFile, Platform, TemplateGallery
)

# Register your models here.

admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(TemplateGallery)

class FileInline(admin.StackedInline):
    model = TemplateFile
    extra = 1

class ImageInline(admin.StackedInline):
    model = TemplateGallery
    extra = 1


class TemplateAdmin(admin.ModelAdmin):
    inlines = (FileInline, ImageInline)
    list_filter = ("category", )
    search_fields = ("name",)

admin.site.register(Template, TemplateAdmin)

class TemplateFileAdmin(admin.ModelAdmin):
    list_display = ("template", "platform")
    list_filter = ("template__category", "platform")

admin.site.register(TemplateFile, TemplateFileAdmin)

