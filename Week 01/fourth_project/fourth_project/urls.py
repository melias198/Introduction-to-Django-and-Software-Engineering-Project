
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',include('first_app.urls')),
    path('home/',include('common_app.urls')),
    path('contact/',include('second_app.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
