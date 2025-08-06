from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer
from django.contrib.auth.models import User

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
