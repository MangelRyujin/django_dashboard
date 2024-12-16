from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from apps.products.models import Product

def sitemap(request):
    """Sitemap txt"""
    # Get all published products
    products_published = list(filter(lambda product: product.is_active, Product.objects.all()))
    products_all_urls = list(map(lambda product: product.get_absolute_url, products_published))
    # Remove empty lines
    text_with_empty_lines = render_to_string(
        "txts/sitemap.txt",
        {
            "products": products_all_urls,
            "domain": settings.DOMAIN_URL,
        },
    )
    text_without_empty_lines = "\n".join([line.strip() for line in text_with_empty_lines.splitlines() if line.strip()])
    # Render sitemap txt
    return HttpResponse(text_without_empty_lines, content_type="text/plain")