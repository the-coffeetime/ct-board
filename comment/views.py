import rest_framework.request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comments, CommentFollowers
from comment.serializers import CommentSerializer, CommentFollowerSerializer


class CommentDetailView(APIView):
    def get(self, request: rest_framework.request.Request):
        post_id = request.query_params.get('postID')

        if post_id is None:
            return Response({'error': 'Missing required parameter'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            post_id = int(post_id)
        except ValueError:
            return Response({'error': 'Invalid postID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            comments = Comments.objects.filter(postID=post_id).order_by('commentID')
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: rest_framework.request.Request):
        serializer = CommentSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request: rest_framework.request.Request):
        comment_id = request.query_params.get('commentID')
        if comment_id is None:
            return Response({'error': 'Missing required parameter'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            comment_id = int(comment_id)
        except ValueError:
            return Response({'error': 'Invalid commentID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            comment = Comments.objects.get(commentID=comment_id)
            comment.delete()
            return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Comments.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_followers(request: rest_framework.request.Request):
    comment_id = request.query_params.get('commentID')
    user_id = request.query_params.get('userID')

    if comment_id is not None:
        try:
            comment_id = int(comment_id)
        except ValueError:
            return Response({'error': 'Invalid commentID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            followers = CommentFollowers.objects.filter(commentID=comment_id)
            follower_list = []
            for follower in followers:
                follower_list.append(follower.userID)
            return Response({'followers': follower_list}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif user_id is not None:
        try:
            user_id = int(user_id)
        except ValueError:
            return Response({'error': 'Invalid userID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            comments = CommentFollowers.objects.filter(userID=user_id)
            serializer = CommentFollowerSerializer(comments, many=True)
            comment_list = []
            for comment in serializer.data:
                comment_list.append(comment['commentID'])
            return Response({'comments': comment_list}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'error': 'Missing required parameter'}, status=status.HTTP_400_BAD_REQUEST)
