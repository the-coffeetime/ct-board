from django.urls import path

from . import views

# 1. postID로 comment 목록 조회 - /api/comment?postID=1
# 2. insert comment - /api/comment
# 3. update comment - /api/comment
# 4. delete comment - /api/comment?commentID=1
# 5. commentID로 follower userID 목록 조회 - /api/comment/followers?commentID=1
# 6. userID로 following comment 목록 조회 - /api/comment/followers?userID=1
urlpatterns = [
    path('', views.CommentDetailView.as_view(), name='commentDetailView'),
    path('followers', views.get_followers, name='getFollowers'),
]
