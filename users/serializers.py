from django.contrib.auth import get_user_model
from rest_framework import serializers

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
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'], name=validated_data['name'])
        return user