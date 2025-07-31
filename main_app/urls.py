from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LocationViewSet,
    CellViewSet,
    StatViewSet,
    CharacterViewSet,
    CharacterStatViewSet,
)

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'cells', CellViewSet)
router.register(r'stats', StatViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'character-stats', CharacterStatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]