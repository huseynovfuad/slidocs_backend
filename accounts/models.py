from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .generators import create_code_shortcode

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    activation_code = models.CharField(max_length=300, blank=True, null=True)
    code = models.CharField(max_length=300, unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name", "surname", "code"]

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def _str_(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.name.title()} {self.surname.title()}"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = create_code_shortcode(size=20, model_=User)
        return super(User, self).save(*args, **kwargs)