from rest_framework import serializers
from .models import *

class ColoursTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = ColoursToken 
        fields = ('pk', 'token','daterandom')