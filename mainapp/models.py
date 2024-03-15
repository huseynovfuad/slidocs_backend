from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class ContentMixin(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True



class About(ContentMixin):

    class Meta:
        verbose_name_plural = "About Us"


class PrivacyPolicy(ContentMixin):

    class Meta:
        verbose_name_plural = "Privacy Policy"


class TermCondition(ContentMixin):

    class Meta:
        verbose_name_plural = "Term and Conditions"


class RefundPolicy(ContentMixin):

    class Meta:
        verbose_name_plural = "Refund Policy"


def upload_to_contact(instance, filename):
    return f"contact/{instance.email}/{filename}"


class Contact(models.Model):
    fullname = models.CharField(max_length=400)
    email = models.EmailField()
    message = RichTextField()
    attach = models.FileField(upload_to=upload_to_contact, blank=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = "Contact"



def upload_to_sliders(instance, filename):
    return f"sliders/{filename}"

class Slider(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to=upload_to_sliders)
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sliders"