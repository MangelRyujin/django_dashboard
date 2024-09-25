from django.db import models
from django.utils.translation import gettext as _
from solo.models import SingletonModel
# Create your models here.

class PrincipalHeader(SingletonModel):
    principal_title = models.CharField(_("Principal comment"),max_length=50,null=True,blank=True)
    secundary_title = models.CharField(_("Secundary comment"),max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = _("Header")
        verbose_name_plural = _("Headers")

    def __str__(self):
        return f'{self.pk}'
    
class SocialMedia(SingletonModel):
    twitter= models.URLField(_("Twitter"),null=True,blank=True)
    instagram= models.URLField(_("Instagram"),null=True,blank=True)
    facebook= models.URLField(_("Facebook"),null=True,blank=True)
    image = models.ImageField(_("Logo"),upload_to="logo_site",null=True,blank=True)
    
    class Meta:
        verbose_name = _("SocialMedia")
        verbose_name_plural = _("SocialMedias")

    def __str__(self):
        return f'{self.pk}'
    
class WhatsAppContact(SingletonModel):
    contact_whatsapp= models.URLField(_("Contact whatsapp"),max_length=255,null=True,blank=True)
    is_active = models.BooleanField(_("Active"),default=False)
    
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.contact_whatsapp
    
class LocalSales(SingletonModel):
    is_active = models.BooleanField(_("Active"),default=True)
    
    class Meta:
        verbose_name = _("Local sales")
        verbose_name_plural = _("Local sales")

    def __str__(self):
        return f'{self.is_active}'
    
class ShopSales(SingletonModel):
    is_active = models.BooleanField(_("Active"),default=True)
    
    class Meta:
        verbose_name = _("Shop sales")
        verbose_name_plural = _("Shop sales")

    def __str__(self):
        return f'{self.is_active}'


