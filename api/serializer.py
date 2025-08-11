from rest_framework import serializers
from api.models import Daily_task, Long_term_goals, CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'id', 'username', 'password', 'email', 'profile_pic', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'profile_pic', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            "user": {
                "id": instance.id,
                "username": instance.username,
                "email": instance.email,
                "phone_number": instance.phone_number,
                "profile_pic": instance.profile_pic.url if instance.profile_pic else None
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_task
        fields = '__all__'
        extra_kwargs = {'author': {'read_only': True}}

class LongTermSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(input_formats=["%Y/%m/%d", "%d/%m/%Y"])  
    end_date = serializers.DateField(input_formats=["%Y/%m/%d", "%d/%m/%Y"])
    class Meta:
        model = Long_term_goals
        fields = '__all__'
        extra_kwargs = { 'author' : {'read_only' : True}}