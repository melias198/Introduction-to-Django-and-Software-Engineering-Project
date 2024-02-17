from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

# function based view
# def base(request):
#     return render(request,'base.html')

# class based view
class BaseTemplateView(TemplateView):
    template_name = 'base.html'
    
# class based view
class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name':'Elias','age':23}
        print(kwargs)
        print(context)
        context.update(kwargs)
        print(context)
        return context


# def store_book(request):
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save(commit=True)
#             print(book.cleaned_data)
#             return redirect('show_book')
#     else:
#         book = BookStoreForm()
    
#     return render(request,'store_book.html',{'form':book})

# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     success_url = reverse_lazy('show_book')
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect('show_book')

class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_book')
    


# def show_book(request):
#     book = BookStoreModel.objects.all()
#     print(book)
#     return render(request,'show_book.html',{'data':book})


# class based view
class ShowBookList(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'data'
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(genre = 'Islamic')
    # def get_queryset(self):
    #     return BookStoreModel.objects.all().order_by('author')
    ordering = ['id']
    
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'


# def edit_book(request,id):
#     book = BookStoreModel.objects.get(pk = id)
#     form = BookStoreForm(instance = book)
#     if request.method == 'POST':
#         form = BookStoreForm(request.POST,instance = book)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('show_book')
    
#     return render(request,'store_book.html',{'form':form})

class BookEditView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_book')


# def delete_book(request,id):
#     BookStoreModel.objects.get(pk = id).delete()
#     return redirect('show_book')

class BookDeleteView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('show_book')
    