from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords
from django.core.validators import MinLengthValidator

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=False,null=False,unique=True)
    image = models.ImageField(_("Image"),upload_to="users_images",null=True,blank=True)
    phone_number = models.CharField(_("Phone number"),max_length=20,null=True,blank=True)
    country = models.CharField(_("Country"), max_length=255,null=True,blank=True)
    city = models.CharField(_("Country"),max_length=255, null=True,blank=True)
    address = models.CharField(_("Address"),max_length=255, null=True,blank=True)
    ci = models.CharField(_("CI"),max_length=11,validators=[MinLengthValidator(11)],unique=True, null=True,blank=True)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True),)