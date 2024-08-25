from typing import Iterable
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator,MaxValueValidator
from simple_history.models import HistoricalRecords
from apps.accounts.models import User
import uuid
# Create your models here.


class Category(models.Model):
    name = models.CharField(_("Name"),max_length=30,unique=True)
    image = models.ImageField(_("Image"),upload_to="category_images")
    is_active = models.BooleanField(_("Active"),default=True)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True),)
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
    

    
class Product(models.Model):
    code = models.CharField(_("Code"),max_length=50,unique=True)
    name = models.CharField(_("Name"),max_length=30,unique=True)
    categories = models.ManyToManyField(Category,_("Categories"),verbose_name="categories_product")
    stars= models.PositiveIntegerField(_("Stars"),validators=[MinValueValidator(1),MaxValueValidator(5)],default=3)
    stock = models.PositiveIntegerField(_("Stock"),default=0)
    price = models.DecimalField(_("Price"), decimal_places= 2,max_digits=12, validators=[MinValueValidator(0.01)])
    image_one = models.ImageField(_("Image"),upload_to="product_images")
    image_two = models.ImageField(_("Image"),upload_to="product_images",null=True,blank=True)
    image_three = models.ImageField(_("Image"),upload_to="product_images",null=True,blank=True)
    is_active = models.BooleanField(_("Active"),default=True)
    small_description = models.TextField(_("Small description"),max_length=255)
    long_description = models.TextField(_("Long description"),max_length=500)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True),)  
     
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
    
    def rating(self):
        return [i for i in range(int(self.stars))]
    
class Coupon(models.Model):
    code  = models.UUIDField(
        _("Code"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="product_coupon")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="user_coupon")
    discount = models.DecimalField(_("Discount"), decimal_places= 2,max_digits=4, validators=[MinValueValidator(0.01)])
    is_active = models.BooleanField(_("Active"),default=True)
    is_exhausted = models.BooleanField(_("Exhausted"),default=False)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True),)  
    
    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def __str__(self):
        return f'{self.code}'
  