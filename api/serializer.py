from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Daily_task, Long_term_goals


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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