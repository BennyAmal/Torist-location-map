from rest_framework import serializers
from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(required=False)
    class Meta:
        model = Destination
        fields = '__all__'
