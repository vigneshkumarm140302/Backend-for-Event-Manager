from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Backend-for-Event-Manager/admin/', admin.site.urls),
    path('Backend-for-Event-Manager/api/', include('api.urls')),
    path('Backend-for-Event-Manager/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('Backend-for-Event-Manager/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
