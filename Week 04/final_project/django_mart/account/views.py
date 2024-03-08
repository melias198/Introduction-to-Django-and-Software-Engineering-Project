from django.shortcuts import render,redirect,reverse
from .forms import RegistrationForm,UpdateForm
from django.contrib.auth import login,logout,authenticate
from cart.models import Cart,CartItem
from order.models import Order,OrderProduct,Payment

# Create your views here.
def create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def register(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    return render(request,'account/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password=password)
        if user is not None:
            session_key = create_session(request)
            print('login er somoy: ',session_key)
            cart = Cart.objects.filter(cart_id = session_key).exists()
            print('Duru :',cart)
            if cart:
                cart = Cart.objects.get(cart_id = session_key)
                print('shalar cart: ',cart)
                is_cart_item_exist = CartItem.objects.filter(cart = cart).exists()
                print(is_cart_item_exist)
                if is_cart_item_exist:
                    cart_item = CartItem.objects.filter(cart = cart)
                    for item in cart_item:
                        item.user = user
                        item.save()
                
            login(request,user)
            return redirect('home')
            
    return render(request,'account/signin.html')


def profile(request):
    return render(request,'account/dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def user_update(request):
    user = request.user
    form = UpdateForm(instance=user)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request,'account/update.html',{'form':form})
        
    


def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'account/order_history.html',{'orders':orders})


def order_details(request,id):
    order = Order.objects.get(id=id)
    order_product = OrderProduct.objects.filter(order=order)
    
    product_total = 0
    for product in order_product:
        product_total += product.product.price*product.quantity
    
    tax = (product_total*2)/100
    
    return render(request,'account/order_details.html',{'order':order,'order_product':order_product,'product_total':product_total,'tax':tax})


def transaction_history(request):
    transactions = Payment.objects.filter(user=request.user)
    return render(request,'account/transaction.html',{'transactions':transactions})


def transaction_details(request,id):
    order_obj = Order.objects.get(payment__id=id)
    print(order_obj.id)
    return redirect(reverse('order_details', args=[order_obj.id]))


def order_complete(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'account/received_order.html',{'orders':orders})