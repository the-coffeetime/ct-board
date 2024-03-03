from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('field/', include('field.urls')),
    path('job/', include('job.urls')),
    path('board/', include('board.urls')),
    path('comment/', include('comment.urls')),
    path('post/', include('post.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]