"""
URL configuration for django_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from apps.general.views import  dashboard_view, login_view, change_password_view,change_password_form
from django.contrib.auth.views import LogoutView,PasswordChangeView
from django.urls import reverse_lazy

urlpatterns = [
    path('admin_django/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
    path('',dashboard_view,name='dashboard_view'),
    path('login/',login_view,name='login_view'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('admins/',include('apps.accounts.urls.admin_urls')),
    path('change_password/',change_password_view,name='change_password_view'),
    path('change_password_form/',change_password_form,name='change_password_form'),
    # path('change_password/',PasswordChangeView.as_view(template_name="password_change.html",success_url = reverse_lazy("login_view")),name='change_password'),
    
]
