from rest_framework import serializers
from .models import *
# Create your views here.

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'