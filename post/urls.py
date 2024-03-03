from django.urls import path

from . import views

# 1. postID로 게시글 조회
# 2. boardID로 게시글 목록 조회, postID 몇 번부터 몇개 범위 지정 (페이징)
# : boardID로 postID 리스트만 먼저 다 가져오고 (커버링 인덱스) 그 다음에 postID 범위로 게시글 정보 조회
# 3. insert post
# 4. update post
# 5. delete post
# 6. postID로 follower userID 목록 조회
urlpatterns = [
    path('posts/<int:postID>/', PostDetailView.as_view, name='postDetailView'),  # post crud (1, 3, 4, 5)
]
