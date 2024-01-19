from rest_framework import serializers
from .models import mysite

class mysiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = mysite
        fields = '__all__'

