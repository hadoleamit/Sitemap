"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap # new
from django.urls import path,include
from recipes.models import Recipe # new

info_dict = {
    'queryset': Recipe.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('sitemap.xml', sitemap, # new
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
