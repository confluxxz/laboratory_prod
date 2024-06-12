from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views.research import ResearchModelViewSet

research_router = SimpleRouter()

research_router.register(prefix='researches', viewset=ResearchModelViewSet, basename='research')

urlpatterns = [
    path('', include(research_router.urls)),
]
