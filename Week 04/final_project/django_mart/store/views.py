from django.shortcuts import render,redirect
from .models import Product,ProductReview
from category.models import Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from order.models import Order,OrderProduct,Payment
from .forms import ReviewForm


# Create your views here.
def store(request,category_slug=None):  
    category = None  
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(is_available = True,category=category)
        page = request.GET.get('page')
        paginator = Paginator(products, 3)
        page_obj = paginator.get_page(page)
        
    else:
        products = Product.objects.filter(is_available = True)
        page = request.GET.get('page')
        paginator = Paginator(products, 6)
        page_obj = paginator.get_page(page)
        
    categories = Category.objects.all()
    total_length = 0
    if category_slug:
        total_length = len(products)
    
    context = {'categories':categories,'products':page_obj,'length':total_length,'category_name':category}
    return render(request,'store/store.html',context)

# Search
def search_view(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query', '')
        products = Product.objects.filter(product_name__icontains = search_query)
        categories = Category.objects.all()
        
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        
        total = len(products)
        context = {'categories':categories,'products':page_obj,'search_query': search_query,'total':total}
        return render(request,'store/search.html',context)
    else:
        return HttpResponse(status=405)


def product_datil(request,category_slug,product_slug):
    product = Product.objects.get(slug=product_slug,category__slug=category_slug)
    
    reviews = ProductReview.objects.filter(product=product)
    user_review = ProductReview.objects.filter(user=request.user, product=product)
    order_product = None
    form = None
    
    if request.user.is_authenticated:
        order_product = OrderProduct.objects.filter(user=request.user,product__slug=product_slug).exists()
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.product = product
                review.save()
                return redirect('product_detail',category_slug,product_slug)
    print(user_review)
    if not user_review: 
        form = ReviewForm()       
    return render(request,'store/product-detail.html',{'product':product,'order_product':order_product,'form':form,'reviews':reviews})
