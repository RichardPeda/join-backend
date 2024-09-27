from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'id', 'name']
        extra_kwargs = {
            'password' : {'write_only': True},
            'id' : {'read_only': True}
        }
    
    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        if(name == 'guest' and email == 'demo123456@mail.com'):
            try:
                user = User.objects.get(email=validated_data['email'], password=validated_data['password'], name=validated_data['name'])
                return user
            except ObjectDoesNotExist:
                user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'], name=validated_data['name'])
                return user
            

        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'], name=validated_data['name'])
        return user
    
class LogoutSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['email', 'password', 'name']