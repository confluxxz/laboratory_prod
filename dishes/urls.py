from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.dishes import DishesModelViewSet


dishes_router = SimpleRouter()
dishes_router.register(prefix='dishes', viewset=DishesModelViewSet, basename='dishes')

urlpatterns = [
    path('', include(dishes_router.urls)),
]
