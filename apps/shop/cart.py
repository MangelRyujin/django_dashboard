from decimal import Decimal
from apps.general.models import ShopSales
from apps.products.models import Product
from django.conf import settings 
from django.contrib import messages

from apps.sales.models import ShopOrder, ShopOrderItem

class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
        self.shop=ShopSales.objects.first()
        
    
    def disabled(self):
        if self.shop.is_active is False:
            self.clear_items()
            return False
        return True
        
    def add_cart(self,product,cant):
        product_id = str(product.id)
        if cant<1:
          self.remove(product)
        else:
            if product_id not in self.cart.keys():
                self.cart[product_id] = {
                    'pk':product.pk,
                    'cant':cant or 0,
                    'price': float(round((product.price - (product.price*product.discount)/100) * cant,2)),
                    'product_name': product.name,
                    'product_image': product.image_one.url,
                    'message':'',
                    }
            else:
                self.cart[product_id]['cant'] = cant
                self.cart[product_id]['price'] = float(round((product.price - (product.price*product.discount)/100) * cant,2))
        self.save()
        return True
    
    def  add_message_product(self, product,message):
        product_id = str(product.id)
        
        if product_id not in self.cart.keys():
            pass
        else:
            self.cart[product_id]['message'] = message or ''
        self.save()
        return True
    
    def increment(self,product):
        product_id = str(product.id)
        if product_id not in self.cart.keys():
                self.cart[product_id] = {
                    'pk':product.pk,
                    'cant': 1,
                    'price': float(round((product.price - (product.price*product.discount)/100),2)),
                    'product_name': product.name,
                    'product_image': product.image_one.url,
                    'message':'',
                    }
        else:
                self.cart[product_id]['cant'] = self.cart[product_id]['cant'] + 1
                self.cart[product_id]['price'] = float(round((product.price - (product.price*product.discount)/100) * self.cart[product_id]['cant'],2))
        self.save()
        return True
    
    def decrement(self,product):
        product_id = str(product.id)
        if self.cart[product_id]['cant'] == 1:
                self.remove(product)
        else:  
                self.cart[product_id]['cant'] = self.cart[product_id]['cant'] -1
                self.cart[product_id]['price'] = float(round((product.price - (product.price*product.discount)/100) * self.cart[product_id]['cant'],2))
        self.save()
        return True
    
    def item_in_cart(self,product):
        if str(product.id) not in self.cart.keys():
            return True
        return False
        
        
    def remove(self, product):
         product_id = str(product.id)
         if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def save(self) :
        self.session.modified=True
        
    
            
    def clear_items(self):
        self.session['cart']={}
        self.session.modified=True
        
    def __iter__(self):      
        cart = self.cart.copy()        
        for item in cart.values():
            item['cant']= item['cant']
            item['price']= item['price']    
            yield item
            
         
    def  get_cant_product(self, product):
        if str(product.id) in self.cart.keys():
            return self.cart[str(product.id)]['cant']
        return 0 
    
    def  get_message_product(self, product):
        if str(product.id) in self.cart.keys():
            return self.cart[str(product.id)]['message'] or ''
        return ''
    
    def get_price_product(self,product):
        if str(product.id) in self.cart.keys():
            return round(self.cart[str(product.id)]['price'],2)
        return 0 
    
    
    def get_total_price(self):
        return round(sum(item['price'] for item in self.cart.values()),2)
    
    def get_total_items(self):
        return sum(item['cant'] for item in self.cart.values())
    
    
    def create_shop_order(self,post):
        shop_order=ShopOrder.objects.create(
            created_user= self.request.user,
            delivery= False if post.get('deliveryCheck') else True,
            message=post['message'] or '',
            phone=post['phone'] or '',
            address=post['address'] or '',
            
        )
        for item in self.cart.values():
            ShopOrderItem.objects.create(
                order = shop_order,
                product= Product.objects.filter(pk=item['pk']).first(),
                cant= item['cant'],
                price= item['price'],
                message = item['message']
            )
        self.clear_items()
        