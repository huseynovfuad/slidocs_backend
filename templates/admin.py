from django.contrib import admin
from .models import (
    Category, Template, TemplateFile, Platform,
)

# Register your models here.

admin.site.register(Category)
admin.site.register(Platform)

class FileInline(admin.StackedInline):
    model = TemplateFile
    extra = 1

class TemplateAdmin(admin.ModelAdmin):
    inlines = (FileInline, )
    list_filter = ("category", )
    search_fields = ("name",)

admin.site.register(Template, TemplateAdmin)

class TemplateFileAdmin(admin.ModelAdmin):
    list_display = ("template", "platform")
    list_filter = ("template__category", "platform")

admin.site.register(TemplateFile, TemplateFileAdmin)

