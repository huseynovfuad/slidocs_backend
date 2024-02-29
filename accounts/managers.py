from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError("You must provide a valid email address.")

    def create_user(self, name, surname, email, password, **extra_fields):
        if not name:
            raise ValueError("Users must have a first name.")
        if not surname:
            raise ValueError("Users must have a last name.")
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Users must have an email address.")

        user = self.model(
            name=name, surname=surname, email=email, **extra_fields
        )
        user.set_password(password)

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)
        return user

    def create_superuser(self, name, surname, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        if not password:
            raise ValueError("Superuser must have a password.")

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Superuser must have an email address.")

        user = self.create_user(name, surname, email, password, **extra_fields)
        user.save(using=self._db)
        return user