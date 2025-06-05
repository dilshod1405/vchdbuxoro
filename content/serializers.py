from .models import (
    Information,
    Service,
    Message
)
from rest_framework import serializers

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        

class MessageSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('created_at',)
        
    def validate_phone(self, value):
        if not value.isdigit() or len(value) != 9:
            raise serializers.ValidationError("Telefon raqami 13 belgidan iborat bo'lishi kerak.")
        return value