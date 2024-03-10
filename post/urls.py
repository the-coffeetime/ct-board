from django.urls import path

from . import views
from .views import PostDetailView

# 1. postID로 게시글 조회 - /api/post?postID=1
# 2. boardID로 게시글 목록 조회, postID 몇 번부터 몇개 범위 지정 (페이징)
# - boardID로 postID 리스트만 먼저 다 가져오고 (커버링 인덱스) 그 다음에 postID 범위로 게시글 정보 조회
# - /api/post?boardID=1&start=50&size=10 (size 없으면 10개, start 없으면 0번부터 전부)
# 3. insert post - /api/post
# 4. update post - /api/post
# 5. delete post - /api/post?postID=1
# 6. postID로 follower userID 목록 조회 - /api/post/followers?postID=1
urlpatterns = [
    path('', PostDetailView.as_view(), name='postDetailView'),
    path('followers', views.get_followers, name='getFollowers')
]
