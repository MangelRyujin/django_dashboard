from django.conf import settings
from django.urls import reverse
from django import template

register = template.Library()


@register.simple_tag
def url_absolute(page):
    return settings.DOMAIN_URL + reverse(page)