from typing import Iterable
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator,MaxValueValidator
from simple_history.models import HistoricalRecords
from apps.accounts.models import User
import uuid
import math
from django.conf import settings
from decimal import Decimal
# Create your models here.


class Offert(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    description = models.CharField(_("Description"),max_length=255)
    init_date = models.DateField(_("Init date"),auto_now=False,auto_now_add=False)
    end_date = models.DateField(_("End date"),auto_now=False,auto_now_add=False)
    image = models.ImageField(_("Image"),upload_to="offert_images")
    is_active = models.BooleanField(_("Active"),default=True)

    class Meta:
        verbose_name = _("Offert")
        verbose_name_plural = _("Offerts")

    def __str__(self):
        return self.name
    
class PrincipalCategory(models.Model):
    name = models.CharField(_("Name"),max_length=30,unique=True)
    image = models.ImageField(_("Image"),upload_to="category_images")
    is_active = models.BooleanField(_("Active"),default=True)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True),)
    

    class Meta:
        verbose_name = _("Principal category")
        verbose_name_plural = _("Principal categories")

    def __str__(self):
        return self.name

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
    name = models.CharField(_("Name"),max_length=70,unique=True)
    views = models.PositiveIntegerField(_("Views"),default=0)
    categories = models.ManyToManyField(Category,_("Categories"),verbose_name="categories_product")
    principal_categories = models.ManyToManyField(PrincipalCategory,verbose_name="principal_category_product")
    likes = models.ManyToManyField(User,verbose_name="likes_product",blank=True)
    stars= models.PositiveIntegerField(_("Stars"),validators=[MinValueValidator(1),MaxValueValidator(5)],default=3)
    total_sales = models.PositiveIntegerField(_("Total sales"),default=0)
    discount = models.DecimalField(_("Discount"), decimal_places= 2,max_digits=12,default=0, validators=[MinValueValidator(0)])
    price = models.DecimalField(_("Price"), decimal_places= 2,max_digits=12, validators=[MinValueValidator(0.01)])
    image_one = models.ImageField(_("Image"),upload_to="product_images")
    image_two = models.ImageField(_("Image"),upload_to="product_images",null=True,blank=True)
    image_three = models.ImageField(_("Image"),upload_to="product_images",null=True,blank=True)
    is_active = models.BooleanField(_("Active"),default=True)
    small_description = models.TextField(_("Small description"),max_length=255)
    long_description = models.TextField(_("Long description"),max_length=500)
    weight = models.DecimalField(_("Price"), decimal_places= 2,max_digits=12,default=0, validators=[MinValueValidator(0)])
    brand = models.CharField(_("Brand"),max_length=50,blank=True,null=True)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True),)  
     
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self): # Nuevo
        return reverse("shop_product_detail_view", kwargs={"pk": f'{self.pk}'})
    
    def rating(self):
        return [i for i in range(int(self.stars))]
    
    def user_has_like(self,user):
        if self.likes.filter(id=user).exists():
            return True
        return False
    
    @property
    def format_views(self):
        if self.views >= 1000000 :
            return f"{math.floor(self.views / 1000000)} M"
        elif self.views >= 1000 and self.views < 1000000:
            return f"{math.floor(self.views / 1000)} Mil"
        else:
            return str(self.views)
    
    @property
    def total_stock(self):
        try:
            return sum(stock.cant for stock in self.product_stock.all() if stock.cant > 0) or 0
        except ValueError:
            return 0
        
    @property
    def total_price(self):
        if self.discount > 0:
            return round(self.price - (round((self.price * self.discount),2) / 100),2)
        else:
            return self.price
        
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
  
class ProductReview(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="product_review")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="user_review")
    message = models.TextField(_("Messagge"), max_length=120,null=None,blank=None)
    is_active = models.BooleanField(_("Active"),default=False)
    stars= models.PositiveIntegerField(_("Stars"),validators=[MinValueValidator(1),MaxValueValidator(5)],default=3)
    create_date = models.DateTimeField(_("Create date"),auto_now_add=True,auto_now=False)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True),)  
    
    class Meta:
        verbose_name = _("Product review")
        verbose_name_plural = _("Product reviews")

    def __str__(self):
        return f'{self.id} by user {self.user.username}'
    
    def rating(self):
        return [i for i in range(int(self.stars))]