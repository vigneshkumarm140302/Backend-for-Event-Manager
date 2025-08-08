from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserSerializer, TaskSerializer, LongTermSerializer
from django.contrib.auth.models import User
from api.models import Daily_task, Long_term_goals

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class TaskView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Daily_task.objects.filter(author = self.request.user).order_by("date")
    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)
    

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
        return Long_term_goals.objects.filter(author = self.request.user).order_by('start_date')
    
class LongTermUpdateView(generics.UpdateAPIView):
    serializer_class = LongTermSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Long_term_goals.objects.filter(author=self.request.user)