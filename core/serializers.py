from rest_framework import serializers
from .models import *

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Username
        fields = ["id", "name", ""]