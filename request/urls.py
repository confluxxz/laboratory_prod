from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.request import RequestModelViewSet


request_router = SimpleRouter()
request_router.register(prefix='request', viewset=RequestModelViewSet, basename='request')

urlpatterns = [
    path('', include(request_router.urls)),
    path('requests/<int:request_id>/', include(request_router.urls)),
]
