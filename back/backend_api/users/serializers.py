from rest_framework import serializers
from .models import User
from .models import Profile
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProfileSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для профиля пользователя.
    """
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'phone_number', 'birth_date']
        ref_name = 'UserProfileSerializer'

class UserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для пользователя, включающий профиль.
    """
    profile = ProfileSerializer()
    # Сериализатор для модели User, используемый для преобразования данных пользователя

    class Meta:
        model = User
        # Поля, которые будут включены в сериализацию
        fields = [
            "email",
            "first_name",
            "last_name",
            "username",
            "city",
            "region",
            "address",
            "phone",
            "photo",
            "profile"
        ]
        # fields = '__all__'
        # Установка полей только для чтения(не меняются)
        read_only_fields = ('email', 'username', 'profile')


    #redacting 'username' field depending on 'first_name' and 'last_name'
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.username = f"{instance.first_name} {instance.last_name}"
        
        profile.avatar = profile_data.get('avatar', profile.avatar)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.birth_date = profile_data.get('birth_date', profile.birth_date)
        profile.save()

        return super().update(instance, validated_data)

class RegisterSerializer(serializers.ModelSerializer):
    password_conf = serializers.CharField(write_only=True)  # Поле для подтверждения пароля

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'password_conf', "city", "region", "address", "phone")

    def create(self, validated_data):
        # Удаляем поле 'password_conf' из validated_data перед созданием пользователя
        password_conf = validated_data.pop('password_conf', None)
        
        # Создаем пользователя с использованием метода create_user вашей модели User
        user = User.objects.create_user(**validated_data)

        # Устанавливаем пароль для пользователя
        user.set_password(validated_data['password'])

        user.username = f"{user.first_name} {user.last_name}"
        user.save()

        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    # Сериализатор для подтверждения электронной почты

    # Добавление поля для токена
    token = serializers.CharField(max_length=600)

    class Meta:
        model = User
        # Поля, которые будут включены в сериализацию
        fields = ['token']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Include additional user data in the response
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            "username": self.user.username,
            'photo': str(self.user.photo) if self.user.photo else None,
            "city": self.user.city,
            "region": self.user.region,
            "address": self.user.address,
            "phone": self.user.phone,
        }
    

        return data


# class ChangePasswordSerializer(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

#     class Meta:
#         ref_name = 'UsersChangePasswordSerializer'  # Уникальное имя ссылки
