from django.urls import path
from core.views import index
from . import views

urlpatterns = [
    path("", index),
    path("battles/", views.get_battles),
    path("teams/", index),
]