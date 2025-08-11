from django.urls import path
from .views import EmailOrPhoneTokenView, UserDetailView, UserUpdateView, UserRegisterView, TaskView, LongTermView, LongTermDeleteView, LongTermUpdateView, TaskUpdateView, TaskDeleteView
from rest_framework_simplejwt.views import  TokenRefreshView



urlpatterns = [
    path('user-register', UserRegisterView.as_view()),
    path('user-details', UserDetailView.as_view()),
    path('user-update', UserUpdateView.as_view()),
    path('daily-task', TaskView.as_view()),
    path('daily-task-edit/<int:pk>', TaskUpdateView.as_view()),
    path('daily-task-delete/<int:pk>', TaskDeleteView.as_view()),
    path('long-term-goals', LongTermView.as_view()),
    path('long-term-goals-delete/<int:pk>', LongTermDeleteView.as_view()),
    path('long-term-goals-edit/<int:pk>', LongTermUpdateView.as_view()),
    path("token/", EmailOrPhoneTokenView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]