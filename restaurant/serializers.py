from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking


class UserSerializer(serializers.ModelSerializer):
    "This class is used to serialize users objects"
    password = serializers.CharField(
        max_length=200,
        allow_blank=False,
        write_only=True,
        required=True
    )
    class Meta:
        """
        In this class we define the model
        and fields to serialize"""
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'].value,
            email=validated_data['email'].value,
            first_name=validated_data['first_name'].value,
            last_name=validated_data['last_name'].value
        )

        user.set_password(validated_data['password'].value)
        user.save()

        return user

    def validate_password(self, value):
        """
        This function have a custom validation 
        for the password field
        """
        if value is None or value == '':
            raise serializers.ValidationError(
                'Password can not be empty or None'
            )
        return value


class MenuSerializer(serializers.ModelSerializer):
    """This class serialize the menu objects"""
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    """This class serialize the Booking objects"""
    class Meta:
        model = Booking
        fields = '__all__'
