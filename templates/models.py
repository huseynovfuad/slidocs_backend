from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


def upload_to_platform(instance, filename):
    return f"platforms/{slugify(instance.name)}/{filename}"


class Platform(models.Model):
    name = models.CharField(max_length=300)
    icon = models.ImageField(upload_to=upload_to_platform)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Platforms"


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"



def upload_to_templates(instance, filename):
    return f"templates/{slugify(instance.name)}/cover/{filename}"


class Template(models.Model):
    name = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    cover = models.ImageField(upload_to=upload_to_templates)
    slides_num = models.PositiveIntegerField(default=1)
    price = models.FloatField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Templates"



def upload_to_template_files(instance, filename):
    return f"templates/{slugify(instance.template.name)}/files/{filename}"

class TemplateFile(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_to_template_files)
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.template.name

    class Meta:
        verbose_name_plural = "Template Files"



def upload_to_template_gallery(instance, filename):
    return f"templates/{slugify(instance.template.name)}/gallery/{filename}"


class TemplateGallery(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to_template_gallery)

    def __str__(self):
        return self.template.name

    class Meta:
        verbose_name_plural = "Template Gallery"
