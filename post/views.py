from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Posts
from .serializers import PostSerializer


class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]  # JWT 토큰이 필요한 인증 클래스

    def get(self, request, postID):
        post = Posts.objects.filter(postID=postID).first()
        if post:
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, postID):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, postID):
        try:
            post = Posts.objects.get(postID=postID)
            serializer = PostSerializer(post, data=request.data, partial=True)  # partial=True로 부분 업데이트 허용
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Posts.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, postID):
        try:
            post = Posts.objects.get(postID=postID)
            post.delete()
            return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Posts.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
