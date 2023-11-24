"""
URL configuration for firstSite project.

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
from django.urls import path
from main_app.views import index, about, contact_view, view_contact_data, register_request, async_view, fetch_data_from_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact_view, name='contact_view'),
    path('view_contact/', view_contact_data, name="view_contact_data"),
    path("register/", register_request, name="register"),
    path("async_page", async_view, name="async_page"),
    path('api_data', fetch_data_from_api, name="api_data")
]
