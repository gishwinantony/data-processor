# serializers.py
from rest_framework import serializers
from .models import WellData

class WellDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellData
        fields = [ 'oil', 'gas', 'brine']
