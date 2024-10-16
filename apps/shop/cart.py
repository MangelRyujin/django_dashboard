from decimal import Decimal
from apps.products.models import Product
from django.conf import settings 
from django.contrib import messages

class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carro=self.session.get(settings.CARRO_SESSION_ID)
        if not carro:
            carro = self.session[settings.CARRO_SESSION_ID]={}
        self.carro=carro
        
        
    def agregar(self,oferta, adultos,ninnos):
        oferta_id = str(oferta.id)
        hotel = oferta.hotel.id
        oferta_ids = self.carro.keys()
        offer1 = Product.objects.filter(id__in=oferta_ids)
        habitaciones = 1
        if offer1:
            offer = offer1[0]
            if offer.hotel.id != hotel:
                messages.add_message(self.request, messages.INFO, f'La oferta {oferta.nombre.upper()} no pertenece al mismo hotel.')
                return False
            
        if oferta_id not in self.carro.keys():
            self.carro[oferta_id] = {
                'adultos':adultos,
                'ninnos':ninnos,
                'cantidad_habitaciones':habitaciones,
                'total':adultos+ninnos,
                'precio': oferta.precio_adulto * adultos + oferta.precio_primer_ninno * ninnos
                }
            messages.success(self.request,f'Se ha introducido la oferta {oferta.nombre}')
            
        else:
            # print(self.carro[oferta_id]['adultos'])
            self.carro[oferta_id] = {
                'adultos':self.carro[oferta_id]['adultos']+adultos,
                'ninnos':self.carro[oferta_id]['ninnos']+ninnos,
                'cantidad_habitaciones':self.carro[oferta_id]['cantidad_habitaciones']+habitaciones,
                'total':self.carro[oferta_id]['adultos']+adultos+self.carro[oferta_id]['ninnos']+ninnos,
                'precio': oferta.precio_adulto * (self.carro[oferta_id]['adultos']+adultos) + oferta.precio_primer_ninno * (self.carro[oferta_id]['ninnos']+ninnos)
                }
            print(self.carro[oferta_id]['precio'])
            messages.add_message(self.request, messages.INFO, f'Se ha añadido otra habitación de la oferta {oferta.nombre.upper()} .')
            
            
        self.guardar()
        return True
    
        
        
        
    def remove(self, oferta):
         oferta_id = str(oferta.id)
         if oferta_id in self.carro:
            del self.carro[oferta_id]
            self.guardar()
    
    def guardar(self) :
        self.session.modified=True
        
    
            
    def limpiar(self):
        self.session['carro']={}
        self.session.modified=True
        
    def __iter__(self):
             
        ofertas_ids = self.carro.keys() 
               
        # get the product objects and add them to the cart        
        ofertas = Product.objects.filter(id__in=ofertas_ids) 
               
        carro = self.carro.copy()        
        for oferta in ofertas:            
            carro[str(oferta.id)]['oferta'] = oferta  
           
        
        for item in carro.values():
               
            item['total']= item['adultos'] + item['ninnos']
            # item['precio']= item['adultos']*oferta.precio_adulto + item['ninnos'] * oferta.precio_primer_ninno   
            item['precio']= item['adultos']* item['oferta'].precio_adulto + item['ninnos'] * item['oferta'].precio_primer_ninno       
            yield item
         
    def __len__(self):
       
        return sum([item['total'] for item in self.carro.values()])
    
    
    def get_min_reservar(self):
        ofertas_ids = self.carro.keys()
        ofertas = Product.objects.filter(id__in=ofertas_ids)
        min = 0
        for oferta in ofertas:
            if min < oferta.dias_min:
                min = oferta.dias_min
            
        return min
        
        
    def get_total_precio(self):
        return sum(item['precio'] for item in self.carro.values())
    
    def get_con_transporte(self):
        for item in self.carro.values():
            agregar=item['transporte']
        return self.get_total_precio+agregar

    
