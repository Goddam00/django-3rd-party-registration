"""ithome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView # 新增
from .views import register # 新增 register
from .views import  HomePage

urlpatterns = [
    
    # path('admin/', admin.site.urls),
    # # vendors app 有兩個綽號 f-vendors 及 s-vendors
    # path('welcome/', include('vendor.urls', namespace='f-vendors')),
    # path('vendor/', include('vendor.urls', namespace='s-vendors')),
    # path('accounts/', include('django.contrib.auth.urls')), # 新增
    # path('', TemplateView.as_view(template_name='home.html')), # 新增
    # path('register/', register, name='register'),
    
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', HomePage.as_view(), name='home'),
]
