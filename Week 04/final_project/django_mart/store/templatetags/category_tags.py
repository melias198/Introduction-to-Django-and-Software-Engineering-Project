from django import template
from category.models import Category
from cart.models import CartItem

register = template.Library()

@register.simple_tag
def get_categories():
    categories = Category.objects.all()
    return categories


@register.simple_tag
def get_cart(request):
    if request.user.is_authenticated:
        cart = CartItem.objects.filter(user=request.user)
    else:
        session_id = request.session.session_key
        cart = CartItem.objects.filter(cart__cart_id=session_id)
    return cart

