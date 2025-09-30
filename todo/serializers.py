from rest_framework import serializers
from .models import TodoItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        read_only_fields = ['user', 'updated_at']
