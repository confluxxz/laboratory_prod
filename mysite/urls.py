"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from utils.allowed_urls import UrlsWithPermissionsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include(('clients.urls', 'clients'), namespace='clients')),
    path('dishes/', include(('dishes.urls', 'dishes'), namespace='dishes')),
    path('inventory/', include(('inventory.urls', 'inventory'), namespace='inventory')),
    path('student/', include(('student.urls', 'student'), namespace='student')),
    path('instance/named/url/list/allowed/', UrlsWithPermissionsView.as_view(), name='allowed-urls'),
    path('research/', include(('research.urls', 'research'), namespace='research')),
    path('requests/', include(('request.urls', 'request'), namespace='request')),
    path('equipments/', include(('request.urls', 'request'), namespace='request'))

]
