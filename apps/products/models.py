from django.db import models
from django.utils.translation import gettext as _
from simple_history.models import HistoricalRecords
# Create your models here.


class Category(models.Model):
    name = models.CharField(_("Name"),max_length=30)
    image = models.ImageField(_("Image"),upload_to="category_images")
    is_active = models.BooleanField(_("Active"),default=True)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True),)
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    
