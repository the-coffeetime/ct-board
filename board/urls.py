from django.urls import path

from . import views
from .views import BoardDetailView

# 1. field 단위 board 목록 조회 - /api/board?fieldID=1
# 2. job 단위 board 목록 조회 - /api/board?jobID=1
# 3. boardID로 follower userID 목록 조회 - /api/board/followers?boardID=1
urlpatterns = [
    path('', BoardDetailView.as_view, name='boardDetailView'),
    path('followers/', views.get_followers, name='getFollowers')
]
