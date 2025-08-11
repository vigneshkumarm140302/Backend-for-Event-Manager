from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserSerializer, TaskSerializer, LongTermSerializer, UserRegisterSerializer
from api.models import Daily_task, Long_term_goals, CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers

class EmailOrPhoneTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        refresh = self.get_token(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

class EmailOrPhoneTokenView(TokenObtainPairView):
    serializer_class = EmailOrPhoneTokenSerializer

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class TaskView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Daily_task.objects.filter(author = self.request.user).order_by("date")
    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)
    

class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Daily_task.objects.filter(author = self.request.user)
    
class TaskDeleteView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Daily_task.objects.filter(author = self.request.user)

class LongTermView(generics.ListCreateAPIView):
    serializer_class = LongTermSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Long_term_goals.objects.filter(author = self.request.user).order_by('start_date')
    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)

class LongTermDeleteView(generics.DestroyAPIView):
    serializer_class = LongTermSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Long_term_goals.objects.filter(author = self.request.user)
    
class LongTermUpdateView(generics.UpdateAPIView):
    serializer_class = LongTermSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Long_term_goals.objects.filter(author=self.request.user)