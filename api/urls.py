from django.urls import path
from .views import UserView, TaskView, LongTermView, LongTermDeleteView, LongTermUpdateView

urlpatterns = [
    path('', UserView.as_view()),
    path('daily-task', TaskView.as_view()),
    path('long-term-goals', LongTermView.as_view()),
    path('long-term-goals-delete/<int:pk>', LongTermDeleteView.as_view()),
    path('long-term-goals-edit/<int:pk>', LongTermUpdateView.as_view()),
]