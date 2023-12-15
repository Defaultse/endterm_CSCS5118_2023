from rest_framework import serializers
from .models import Moderator, News
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = '__all__'

class ModeratorTokenObtainSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = Moderator.objects.get(username=data.get('username'))

        if not user.check_password(data.get('password')):
            raise serializers.ValidationError("Invalid password")

        refresh = RefreshToken.for_user(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
    

class ModeratorTokenObtainSerializer(TokenObtainPairSerializer):
    class Meta:
        model = Moderator
        fields = ('username', 'password')

# class ModeratorTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         return token

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class CreateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ['moderator']

class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ['moderator']