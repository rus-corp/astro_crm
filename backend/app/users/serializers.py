from rest_framework import serializers


from .models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'email']



class CustomUserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['email', 'password']
