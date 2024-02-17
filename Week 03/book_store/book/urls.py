from django.urls import path
# from book.views import base,store_book,show_book,edit_book,delete_book
from . import views

urlpatterns = [
    # path('',views.base,name="basepage"),
    # path('',views.TemplateView.as_view(template_name = 'base.html'),name='basepage'), Shortcut way without creating view
    path('',views.BaseTemplateView.as_view(),name='basepage'),
    
    path('home/<int:roll>/',views.HomeTemplateView.as_view(),{'author':'Mohammad Elias'}),
    
    # path('store_new_book/',views.store_book,name="store_book"),
    path('store_new_book/',views.BookFormView.as_view(),name="store_book"),
    
    # path('show_books/',views.show_book, name="show_book"),
    path('show_books/',views.ShowBookList.as_view(), name="show_book"),
    
    path('book_details/<int:id>',views.BookDetailsView.as_view(),name='book_details'),
    
    # path('edit_book/<int:id>',views.edit_book, name="edit_book"),
    path('edit_book/<int:pk>',views.BookEditView.as_view(), name="edit_book"),
    
    # path('delete_book/<int:id>',views.delete_book, name="delete_book"),
    path('delete_book/<int:pk>',views.BookDeleteView.as_view(), name="delete_book"),
]
