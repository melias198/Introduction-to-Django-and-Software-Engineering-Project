from django.shortcuts import render,redirect
from store.models import Product
from .models import Cart,CartItem

# Create your views here.
def create_session(request):
    if not request.session.session_key:
        request.session.create()
    
    return request.session.session_key


def cart(request):
    total = 0
    shipping_fee = 0
    cart_items = None
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            total += item.product.price*item.quantity
    else:
        session_id = create_session(request)
        cart = Cart.objects.filter(cart_id=session_id).exists()
        if cart:
            cart_id = Cart.objects.get(cart_id=session_id) 
            cart_items = CartItem.objects.filter(cart=cart_id)
            for item in cart_items:
                total += item.product.price*item.quantity
    
    tax = (2*total)/100
    if total:
        shipping_fee = 10
    final_total = total+tax+shipping_fee
    
    context = {'cart_items':cart_items,'tax':tax,'fee':shipping_fee,'final_total':final_total,'total':total}
    return render(request,'cart/cart.html',context)


def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    session_id = create_session(request)
    print('cart er somoy: ',session_id)
    
    if request.user.is_authenticated:
        cart_id = Cart.objects.filter(cart_id=session_id).exists()
        if cart_id:
            cart_item = CartItem.objects.filter(product=product,user=request.user).exists()
            if cart_item:
                item = CartItem.objects.get(product=product,user=request.user)
                item.quantity += 1
                item.save()
            else:
                cartid = Cart.objects.get(cart_id=session_id)
                cart_item = CartItem.objects.create(
                    user = request.user,
                    product = product,
                    quantity = 1,
                    cart = cartid
                )
                cart_item.save()
        else:
            cart = Cart.objects.create(
                cart_id = session_id
            )
            cart.save()
            
            # New
            cart_item = CartItem.objects.filter(product=product,user=request.user).exists()
            if cart_item:
                item = CartItem.objects.get(product=product,user=request.user)
                item.quantity += 1
                item.save()
            else:
                cartid = Cart.objects.get(cart_id=session_id)
                cart_item = CartItem.objects.create(
                        user = request.user,
                        product = product,
                        quantity = 1,
                        cart = cartid
                    )
                cart_item.save()
            
    else:
        cart_id = Cart.objects.filter(cart_id=session_id).exists()
        print(cart_id)
        if cart_id:
            cart_item = CartItem.objects.filter(product=product,cart__cart_id=session_id).exists() #Updated
            if cart_item:
                item = CartItem.objects.get(user=None,product=product,cart__cart_id=session_id) 
                item.quantity += 1
                item.save()
            else:
                cartid = Cart.objects.get(cart_id=session_id)
                cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    cart = cartid
                )
                cart_item.save()
        else:
            cart = Cart.objects.create(
                cart_id = session_id
            )
            cart.save()
            
            cartid = Cart.objects.get(cart_id=session_id)
            cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    cart = cartid
                )
            cart_item.save()
    
    return redirect('cart')


def remove_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    session_id = request.session.session_key
    cart_id = Cart.objects.get(cart_id=session_id)
    
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(user=request.user,product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    else:
        cart_item = CartItem.objects.get(cart=cart_id,product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        
    return redirect('cart')

def delete_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    session_id = request.session.session_key
    cart_id = Cart.objects.filter(cart_id=session_id).exists()
    if cart_id:
        cart_id = Cart.objects.get(cart_id=session_id)
    
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(user=request.user,product=product)
        cart_item.delete()
    else:
        cart_item = CartItem.objects.get(cart=cart_id,product=product)
        cart_item.delete()
    
    return redirect('cart')


# def checkout(request):
#     total = 0
#     shipping_fee = 0
#     cart_items = None
#     if request.user.is_authenticated:
#         cart_items = CartItem.objects.filter(user=request.user)
#         for item in cart_items:
#             total += item.product.price*item.quantity
#     else:
#         session_id = create_session(request)
#         cart = Cart.objects.filter(cart_id=session_id).exists()
#         if cart:
#             cart_id = Cart.objects.get(cart_id=session_id) 
#             cart_items = CartItem.objects.filter(cart=cart_id)
#             for item in cart_items:
#                 total += item.product.price*item.quantity
    
#     tax = (2*total)/100
#     if total:
#         shipping_fee = 10
#     final_total = total+tax+shipping_fee
#     return render(request,'cart/place-order.html',{'cart_items':cart_items,'tax':tax,'fee':shipping_fee,'final_total':final_total,'total':total})