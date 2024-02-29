from django.db import models
from templates.models import Template
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlist"
        unique_together = [("user", "template")]