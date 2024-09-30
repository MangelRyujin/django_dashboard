from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect

class NoCacheMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # if not request.user.is_authenticated and 'Username or password incorrect' not in str(response.content):
        #         response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        #         response['Pragma'] = 'no-cache'
        #         response['Expires'] = '0'
        #         response["HX-Redirect"]= '/login/'
        return response
