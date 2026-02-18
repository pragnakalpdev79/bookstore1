from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from user import views as user_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/',include('catalog.urls')),
    path('',RedirectView.as_view(url='catalog',permanent=True),name='home'),
    path('login/', user_view.Login, name ='login'),
    path('logout/', user_view.loguout, name ='logout'),
    path('register/', user_view.register, name ='register'),
    
]
