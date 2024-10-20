from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator
from apps.accounts.models import User
from apps.inventory.models import Stock
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
    user_create=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="user_created_order",null=True,blank=True)
    user_id=models.CharField(_("User id"),max_length=255, null=True,blank=True)
    user_ci=models.CharField(_("User ci"),max_length=255, null=True,blank=True)
    user_full_name=models.CharField(_("User full name"),max_length=255, null=True,blank=True)
    user_phone=models.CharField(_("User phone"),max_length=255, null=True,blank=True)
    address=models.CharField(_("Address"),max_length=255, null=True,blank=True)
    type = models.CharField(_("Type"),max_length=1, choices=TYPE_CHOICES, default='l') 
    payment_type = models.CharField(_("Payment type"),max_length=1, choices=PAYMENT_TYPE_CHOICES, default='c') 
    created_date = models.DateTimeField(_("Created date"),auto_now_add=True,auto_now=False)
    cash = models.DecimalField(_("Cash"), decimal_places= 2,max_digits=12,default=0,validators=[MinValueValidator(0)] )
    transfer = models.DecimalField(_("Transfer"), decimal_places= 2,max_digits=12,default=0,validators=[MinValueValidator(0)] )
    

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
    
    @property
    def revenue(self):
        return self.total_price - self.total_cost
        
        
class LocalOrder(models.Model):
    STATE_CHOICES = (
        ('p', _("processing")),
        ('c', _("checked")),
        
    )
    user_create=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="user_created_order")
    state = models.CharField(_("State"),max_length=1, choices=STATE_CHOICES, default='p') 
    created_date = models.DateTimeField(_("Created date"),auto_now_add=True,auto_now=False)
    user_ci=models.CharField(_("User ci"),max_length=255,null=True,blank=True)
    user_first_name=models.CharField(_("User first name"),max_length=255,null=True,blank=True)
    user_last_name=models.CharField(_("User last name"),max_length=255,null=True,blank=True)
    user_phone=models.CharField(_("User phone"),max_length=255,null=True,blank=True)
    address=models.CharField(_("Address"),max_length=255,null=True,blank=True)
    
    
    class Meta:
        verbose_name = _("Local order")
        verbose_name_plural = _("Local orders")

    def __str__(self):
        return f'{self.pk}'
    
    @property
    def total_items(self):
        return sum(item.cant for item in self.localorderitem_set.all()) or 0
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.localorderitem_set.all()) or 0
    
    # Verify existence in order items
    
    def items_exists(self):
        local_order_items=self.localorderitem_set.all()
        if local_order_items.exists():
            for item in local_order_items:
                if item.local_order_items_stocks_exist == False:
                    return False
            return True
        return False
    
    
    # Verify not in order items empty
    @property
    def items_empty_exists(self):
        local_order_items=self.localorderitem_set.all()
        if local_order_items.exists():
            for item in local_order_items:
                if item.local_order_items_stocks_empty_exist == False:
                    return False
            return True
        return False
    
class LocalOrderItem(models.Model):
    order = models.ForeignKey(LocalOrder,on_delete=models.CASCADE,verbose_name="local_order_item")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="local_product_item")

    class Meta:
        verbose_name = _("Local order item")
        verbose_name_plural = _("Local orders items")

    def __str__(self):
        return f'{self.pk}'
    
    @property
    def cant(self):
        return sum(item.cant for item in self.localorderitemstock_set.all()) or 0
    
    @property
    def total_price(self):
        return (self.product.total_price * sum(item.cant for item in self.localorderitemstock_set.all())) or 0
    
    @property
    def total_cost(self):
        return sum(item.price for item in self.localorderitemstock_set.all()) or 0

    # Verify existence in stocks for porducts
    @property
    def local_order_items_stocks_exist(self):
        local_order_item_stocks=self.localorderitemstock_set.all()
        if local_order_item_stocks.exists():
            for stock in local_order_item_stocks:
                if stock.stock_cant_exists == False:
                    return False
            return True
        return False
    
    # Verify existence not stock empty
    @property
    def local_order_items_stocks_empty_exist(self):
        local_order_item_stocks=self.localorderitemstock_set.all()
        if local_order_item_stocks.exists():
            return True
        return False

class LocalOrderItemStock(models.Model):
    item = models.ForeignKey(LocalOrderItem,on_delete=models.CASCADE,verbose_name="local_order_item_stock")
    stock = models.ForeignKey(Stock,on_delete=models.CASCADE,verbose_name="local_stock_item")
    cant= models.PositiveIntegerField(_("Cant"))
    
    class Meta:
        verbose_name = _("Local order item stock")
        verbose_name_plural = _("Local orders items stocks")

    def __str__(self):
        return f'{self.pk}'
    
    @property
    def price(self):
        return self.cant * self.stock.unit_price
    
    @property
    def stock_cant_exists(self):
        if self.stock.cant >= self.cant:
            return True
        return False
    

class ShopOrder(models.Model):
    STATE_CHOICES = (
        ('p', _("processing")),
        ('c', _("checked")),
        
    )
    created_user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="user_created_order")
    state = models.CharField(_("State"),max_length=1, choices=STATE_CHOICES, default='p') 
    created_date = models.DateTimeField(_("Created date"),auto_now_add=True,auto_now=False)
    delivery=models.BooleanField(_("Delivery"),default=True)
    message = models.TextField(_('Message'),null=True,blank=True)
    phone=models.CharField(_("Phone"),max_length=255)
    address=models.CharField(_("Address"),max_length=255)
    
    
    class Meta:
        verbose_name = _("Shop order")
        verbose_name_plural = _("Shop orders")

    def __str__(self):
        return f'{self.pk}'
    
    @property
    def total_items(self):
        return sum(item.cant for item in self.shoporderitem_set.all()) or 0
    
    @property
    def total_price(self):
        return sum(item.price for item in self.shoporderitem_set.all()) or 0
    
    # Verify existence in order items
    
    def items_exists(self):
        shop_order_items=self.shoporderitem_set.all()
        if shop_order_items.exists():
            for item in shop_order_items:
                if item.shop_order_items_stocks_exist == False:
                    return False
            return True
        return False
    
    
    # Verify not in order items empty
    @property
    def items_empty_exists(self):
        shop_order_items=self.shoporderitem_set.all()
        if shop_order_items.exists():
            # for item in shop_order_items:
            #     if item.shop_order_items_stocks_empty_exist == False:
            #         return False
            return True
        return False

    
class ShopOrderItem(models.Model):
    order = models.ForeignKey(ShopOrder,on_delete=models.CASCADE,verbose_name="shop_order_item")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="shop_product_item")
    cant = models.PositiveIntegerField(_('Cant'))
    price = models.DecimalField(_("Price"), decimal_places= 2,max_digits=12,validators=[MinValueValidator(0)])
    message = models.TextField(_('Message'),blank=True,null=True)
    
    
    class Meta:
        verbose_name = _("Shop order item")
        verbose_name_plural = _("Shop orders items")

    def __str__(self):
        return f'{self.pk}'
    
    @property
    def available(self):
        stock_max = sum(stock.cant for stock in Stock.objects.filter(is_active=True,cant__gt=0,product=self.product.pk))
        if stock_max < self.cant:
          return False
        return True
    
    @property
    def missing(self):
        stock_max = sum(stock.cant for stock in Stock.objects.filter(is_active=True,cant__gt=0,product=self.product.pk))
        return (stock_max - self.cant)*(-1)