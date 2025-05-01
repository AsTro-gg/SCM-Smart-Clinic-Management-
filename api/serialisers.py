from rest_framework import serializers
from core import models

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username','password','email','role','address','contacts']

    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role'],
            address=validated_data['address'],
            contacts=validated_data['contacts']
        )
        return user
    


