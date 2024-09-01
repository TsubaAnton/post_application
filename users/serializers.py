from rest_framework import serializers
from .models import User
from .validators import validate_password_strength


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'birth_date', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'phone', 'birth_date', 'password']

    def validate_password(self, value):
        validate_password_strength(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            birth_date=validated_data.get('birth_date'),
        )
        user.set_password(password)
        user.save()
        return user
