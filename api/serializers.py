from rest_framework import serializers

from api.models import BioData

class BioDataSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    hobby = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=13)
    class Meta:
        model = BioData
        fields = '__all__'