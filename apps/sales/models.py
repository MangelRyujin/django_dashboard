from django.db import models
from django.utils.translation import gettext as _

from apps.products.models import Product

# Create your models here.
class Order(models.Model):
    TYPE_CHOICES = (
        ('s', _("shop")),
        ('l', _("local")),
        
    )
    PAYMENT_TYPE_CHOICES = (
        ('c', _("cash")),
        ('t', _("transfer")),
        ('b', _("both")),
        
    )
    
    user_id=models.CharField(_("User id"),max_length=255)
    user_ci=models.CharField(_("User ci"),max_length=255)
    user_full_name=models.CharField(_("User full name"),max_length=255)
    user_phone=models.CharField(_("User phone"),max_length=255)
    address=models.CharField(_("Address"),max_length=255)
    type = models.CharField(_("Type"),max_length=1, choices=TYPE_CHOICES, default='l') 
    payment_type = models.CharField(_("Payment type"),max_length=1, choices=PAYMENT_TYPE_CHOICES, default='c') 
    created_date = models.DateTimeField(_("Created date"),auto_now_add=True,auto_now=False)
    cash = models.DecimalField(_("Cash"), decimal_places= 2,max_digits=12)
    transfer = models.DecimalField(_("Transfer"), decimal_places= 2,max_digits=12)
    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f'{self.pk}'
    
    @property
    def total_price(self):
        if self.payment_type == "c":
            return self.cash
        elif self.payment_type == "t":
            return self.transfer
        else:
            return self.transfer + self.cash
    
    @property
    def total_items(self):
        return sum(item.cant for item in self.orderitem_set.all()) or 0


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="order_items")
    product_id=models.CharField(_("Product id"),max_length=255)
    product_name=models.CharField(_("Product name"),max_length=255)
    cant= models.PositiveIntegerField(_("Cant"))
    total_cost = models.DecimalField(_("Cost"), decimal_places= 2,max_digits=12)
    total_price = models.DecimalField(_("Price"), decimal_places= 2,max_digits=12)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
    
    def __str__(self):
        return f'{self.pk}'
    
    @property
    def image(self):
        product = Product.objects.filter(pk=self.product_id).first()
        if product:
            return product.image_one
        else:
            return False