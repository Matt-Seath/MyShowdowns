from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()
router.register("battles", BattleViewSet)

urlpatterns = router.urls

