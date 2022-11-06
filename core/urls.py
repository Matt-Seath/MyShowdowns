from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from .views import index

router = routers.DefaultRouter()
router.register("battles", views.)

urlpatterns = router.urls + battles_router

