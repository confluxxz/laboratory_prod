from django.urls import path
from tests import views

app_name = 'tests'

urlpatterns = [
    path('test/', views.tests, name='test')
]