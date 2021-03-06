from django import template
from shop import models

register = template.Library()

@register.simple_tag
def number_of_products(request):
    cart_id = request.session.get('cart_id')
    if cart_id is None:
        return 0
    return models.Cart.cart_manager.number_of_products(cart_id)['quantity__sum']