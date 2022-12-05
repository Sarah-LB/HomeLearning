from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):

    wishlist_items = []
    total = 0
    product_count = 0
    wishlist = request.session.get('wishlist', {})

    context = {
        'wishlist_items': wishlist_items,
        'product_count': product_count,
        'total': total,
    }

    return context