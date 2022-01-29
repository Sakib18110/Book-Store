from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class bookseriallizer(serializers.ModelSerializer):
    class Meta:
        model= books
        fields='__all__'

class userseriallizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class orderserializer(serializers.ModelSerializer):
    class Meta:
        model=order_book
        fields='__all__'