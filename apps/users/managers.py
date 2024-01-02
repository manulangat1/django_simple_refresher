from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Incorrect email address"))

    def create_user(
        self, username, email, password, first_name, last_name, **extra_fields
    ):
        if not username:
            raise ValueError(_("You must provide a valid username"))
        if not first_name:
            raise ValueError(_("You must provide a first name"))

        if not last_name:
            raise ValueError(_("You must provide a last name"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Email must be provided"))

        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, email, password, first_name, last_name, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not password:
            raise ValueError(_("Password must "))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Email must be provided"))
        user = self.create_user(
            username, email, password, first_name, last_name, **extra_fields
        )
        user.save(using=self._db)
        return user
