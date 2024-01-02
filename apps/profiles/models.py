from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel


# Create your models here.
class Gender(models.TextChoices):
    MALE = "MALE", _("Male")
    FEMALE = "FEMALE", _("FEMale")
    OTHER = "OTHER", _("OTHER")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+255730212345"
    )
    about_me = models.TextField(verbose_name=_("About Me"), max_length=500, blank=True)
    license = models.CharField(verbose_name=_("License"), max_length=50, blank=True)
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),
        #  upload_to="profile_photos", blank=True,
        default="/profile_default.png",
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=180,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    country = CountryField(
        verbose_name=_("Country"), default="KE", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Nairobi",
        blank=False,
        null=False,
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Is Buyer"),
        default=False,
        help_text="Are you looking to buy a property",
    )
    is_seller = models.BooleanField(
        verbose_name=_("Is Seller"),
        default=False,
        help_text="Are you looking to sell a property",
    )
    is_agent = models.BooleanField(
        verbose_name=_("Is Agent"),
        default=False,
        help_text="Are you looking to rent a property",
    )
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
    )
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"),
        default=0,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username
