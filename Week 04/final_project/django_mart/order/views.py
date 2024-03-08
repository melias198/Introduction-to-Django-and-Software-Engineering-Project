from django.shortcuts import render,redirect
from cart.models import Cart,CartItem
from .forms import OrderForm
from datetime import datetime
from .ssl import sslcommerz_payment_gateway
from .models import Payment, OrderProduct, Order
from store.models import Product
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse


# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch') 
@csrf_exempt
def success_view(request):
    data = request.POST
    user_id = int(data['value_b'])  
    user = User.objects.get(pk=user_id)
    print(user)
    print(data['value_a'])
    or_id = data['value_a']
    payment = Payment(
        user = user,
        payment_id =data['tran_id'],
        payment_method = data['card_issuer'],
        amount_paid = float(data['store_amount']), 
        status =data['status'],
    )
    payment.save()
    
    # working with order model
    order = Order.objects.get(user=user, is_ordered=False, order_number=data['value_a'])
    order.payment = payment
    order.is_ordered = True
    order.save()
    cart_items = CartItem.objects.filter(user = user)
    
    for item in cart_items:
        orderproduct = OrderProduct()
        product = Product.objects.get(id=item.product.id)
        orderproduct.order = order
        orderproduct.payment = payment
        orderproduct.user = user
        orderproduct.product = product
        orderproduct.quantity = item.quantity
        orderproduct.ordered = True
        orderproduct.save()

        # Reduce the quantity of the sold products
        product.stock -= item.quantity 
        product.save()

    # Clear cart
    CartItem.objects.filter(user=user).delete()
    
    # Invoice Details
    order_details = Order.objects.get(user=user,order_number=or_id)
    payment_details = Payment.objects.get(user=user,payment_id=order_details.payment.payment_id)
    product_details = OrderProduct.objects.filter(user=user,payment=payment_details)
    
    product_price = 0
    for i in product_details:
        product_price += i.product.price*i.quantity
    # return redirect('order_complete')
    tax = (2*product_price)/100
    total_price =product_price+tax+10 
    context = {'order_details':order_details,'payment_details':payment_details,'product_details':product_details,'product_price':product_price,'tax':tax,'total_price':total_price}
    return render(request,'order/order_complete.html',context)

    
        

@csrf_exempt
def faild_view(request):
    template_name = 'order/faild_order.html'
    if request.method == 'GET':
        print('get')
        return render(request, template_name)
    elif request.method == 'POST':
        return render(request, template_name)


def order_complete(request):
    return render(request,'order/order_complete.html')


def checkout(request):
    total = 0
    shipping_fee = 0
    cart_items = None
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%Y%m%d")
    
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        if cart_items.count() < 1:
            return redirect('store')
        for item in cart_items:
            total += item.product.price*item.quantity
    else:
        return redirect('login')
    
    tax = (2*total)/100
    if total:
        shipping_fee = 10
    final_total = total+tax+shipping_fee
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.order_total = final_total
            form.instance.tax = tax
            form.instance.ip = request.META.get('REMOTE_ADDR')
            saved_instance = form.save()
            form.instance.order_number = formatted_date+str(saved_instance.id)
            print(form.instance.order_number)
            form.save()
            ord_id = form.instance.order_number
            return redirect(sslcommerz_payment_gateway(request,  ord_id, str(request.user.id), final_total))
    
    return render(request,'order/place-order.html',{'cart_items':cart_items,'tax':tax,'fee':shipping_fee,'final_total':final_total,'total':total})


