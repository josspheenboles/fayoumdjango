"""
URL configuration for libary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.contrib.admin import *
from accounts.views import *
#url--->view function(views.py)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Books/',include('book.urls')),
    path('Authors/',include('author.urls')),
    # path('accounts/login/',views.LoginView.as_view(),name='login'),
    # path('accounts/profile/',views.FormView.as_view(),name='profile'),
    # path('Logout/', views.LogoutView.as_view(),name='logout'),
    path('Register/', register,name='register'),
    path('', login,name='login'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#uuid--->
#slug=ascii,lettwe,number
#str=letter,number
#path--->r-path ---->float