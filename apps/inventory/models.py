from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator,MaxValueValidator

from apps.accounts.models import User
from apps.products.models import Product
# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(_("Name"),max_length=40,unique=True)
    address = models.CharField(_("Address"),max_length=120)

    class Meta:
        verbose_name = _("Warehouse")
        verbose_name_plural = _("Warehouses")

    def __str__(self):
        return self.name

class CategoryStock(models.Model):
    name = models.CharField(_("Name"),max_length=80,unique=True)

    class Meta:
        verbose_name = _("Category Stock")
        verbose_name_plural = _("Categories Stocks")

    def __str__(self):
        return self.name

class Stock(models.Model):
    MEASURE_UNIT_CHOICES = (
        ('m', _("milliliters")),
        ('g', _("grams")),
        ('u', _("units")),
    )
    
    code = models.CharField(_("Code"),max_length=50,unique=True)
    name = models.CharField(_("Name"),max_length=100,unique=True)
    address = models.CharField(_("Address"),max_length=120,blank=True,null=True)
    categories = models.ManyToManyField(CategoryStock,related_name="category_stock") 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_stock")
    is_active = models.BooleanField(_("Active"),default=False)
    warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE,related_name="warehouse_stock",null=True,blank=True)
    measure_unit = models.CharField(_("Measure unit"),max_length=1, choices=MEASURE_UNIT_CHOICES, default='u') 
    expiration_date = models.DateField(_("Expire date"))
    create_date = models.DateTimeField(_("Create date"),auto_now_add=True)
    cant = models.DecimalField(_("Cant"), decimal_places= 2,max_digits=12, validators=[MinValueValidator(0.01)])
    unit_price = models.DecimalField(_("Inversion Cost"), max_digits=12, default=0, decimal_places=2,validators=[MinValueValidator(0.01)])
    
    
    
    class Meta:
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")

    def __str__(self):
        return self.name
    
    
class Supplier(models.Model):
    
    name = models.CharField(_("Name"),max_length=100,unique=True)
    address = models.CharField(_("Address"),max_length=255)
    email = models.EmailField(_("Email address"), blank=False,null=False,unique=True)
    image = models.ImageField(_("Image"),upload_to="suppliers_images",null=True,blank=True)
    phone_number = models.CharField(_("Phone number"),max_length=20,null=True,blank=True)
    
    
    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.name
    
class Facture(models.Model):
    MEASURE_UNIT_CHOICES = (
        ('m', _("milliliters")),
        ('g', _("grams")),
        ('u', _("units")),
    )
    
    code = models.CharField(_("Code"),max_length=50,unique=True)
    description = models.TextField(_("Description"))
    create_date = models.DateTimeField(_("Create date"),auto_now_add=True,editable=False)
    amount = models.DecimalField(_("Amount"), max_digits=12, default=0, decimal_places=2,validators=[MinValueValidator(0.01)])
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name="supplier_facture")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_facture")
    cant = models.DecimalField(_("Cant"), decimal_places= 2,max_digits=12, validators=[MinValueValidator(0.01)])
    measure_unit = models.CharField(_("Measure unit"),max_length=1, choices=MEASURE_UNIT_CHOICES, default='u') 
    
    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.code
    

class StockMovements(models.Model):
    TYPE_CHOICES  = (
        ('1', 'exit'),
        ('2', 'entrance'),
        
    )
    type = models.CharField(_("Type"),max_length=7, choices=TYPE_CHOICES, default='2') 
    created_date = models.DateTimeField(_("Create date"),auto_now_add=True)
    motive = models.CharField(_("Motive"),max_length=255) 
    description = models.TextField(_("Description"),null=True,blank=True)
    cant = models.DecimalField(_("Cant"), max_digits=12, default=0, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False,related_name=_('user_stock_movement'))
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE,null=False,blank=False,related_name=_('stock_movement'))

    class Meta:
        """Meta definition for StockMovements."""

        verbose_name = _("Stock movement")
        verbose_name_plural = _("Stocks Movements")


    def __str__(self):
        return self.pk