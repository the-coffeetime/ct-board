from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/field/', include('field.urls')),
    path('api/job/', include('job.urls')),
    path('api/board/', include('board.urls')),
    path('api/comment/', include('comment.urls')),
    path('api/post/', include('post.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]