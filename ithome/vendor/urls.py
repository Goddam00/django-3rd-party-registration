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
from django.urls import path

from . import views
app_name = 'vendors' # 新增
urlpatterns = [
    #path('', views.showtemplate),
    
    #path('', views.showtemplate, name="index"),
    #path('create', views.vendor_create_view, name = 'create'), # 新增
    #path('<int:id>/', views.singleVendor, name='vendor_id'), # 將 urls.py 加上這一段，我們要將每一個攤販的 id 傳至 views 的 singleVendor
    
    #path('', views.VendorListView, name='index'),
    #path('<int:id>/', views.VendorDetailView, name='vendor_id'),
    path('', views.VendorListView.as_view(), name='index'),
    path('<int:pk>/', views.VendorDetailView.as_view(), name='vendor_id'),
    path('create/', views.VendorCreateView.as_view(), name='create'), # 新增
    path('<int:pk>/update/', views.VendorUpdateView.as_view(), name='update'),
]
