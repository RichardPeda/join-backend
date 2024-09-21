from rest_framework import serializers

from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=30)
    # email = serializers.CharField(max_length=50)
    # phone = serializers.CharField(max_length=20)
    # badge_color = serializers.CharField(max_length=20)
    # initials = serializers.CharField(max_length=2)
    # register = serializers.CharField(max_length=1)
    # selected = serializers.BooleanField(default=False)

    class Meta:
        model = Contact
        fields = '__all__'

    # def create(self, validated_data):
    #     contact = Contact.objects.get_or_create(**validated_data)
    #     return contact