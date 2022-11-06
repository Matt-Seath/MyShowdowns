from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register("battles", BattleViewSet)
router.register("pokemon", PokemonViewSet)
router.register("ability", AbilityViewSet)

urlpatterns = router.urls

