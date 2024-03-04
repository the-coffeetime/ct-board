import rest_framework.request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Posts, PostFollowers
from .serializers import PostSerializer


class PostDetailView(APIView):
    def get(self, request: rest_framework.request.Request):
        post_id = request.query_params.get('postID')
        board_id = request.query_params.get('boardID')

        if board_id is not None:
            try:
                board_id = int(board_id)
            except ValueError:
                return Response({'error': 'Invalid boardID'}, status=status.HTTP_400_BAD_REQUEST)
            start = request.query_params.get('start')
            size = request.query_params.get('size')
            try:
                if start is None:
                    posts = Posts.objects.filter(boardID=board_id).order_by('postID')
                elif size is None:
                    try:
                        start = int(start)
                    except ValueError:
                        return Response({'error': 'Invalid start'}, status=status.HTTP_400_BAD_REQUEST)
                    posts = Posts.objects.filter(boardID=board_id, postID__gte=start).order_by('postID')[:10]
                else:
                    try:
                        start = int(start)
                        size = int(size)
                    except ValueError:
                        return Response({'error': 'Invalid start or size'}, status=status.HTTP_400_BAD_REQUEST)
                    posts = Posts.objects.filter(boardID=board_id, postID__gte=start).order_by('postID')[:size]
                serializer = PostSerializer(posts, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif post_id is not None:
            try:
                post = Posts.objects.get(postID=post_id)
                if post:
                    serializer = PostSerializer(post)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'Missing required parameter'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request: rest_framework.request.Request):
        serializer = PostSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            serializer = PostSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                post_id = serializer.validated_data.get('postID')
                post = Posts.objects.get(postID=post_id)

                serializer = PostSerializer(post, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Posts.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            post_id = int(request.query_params.get('postID'))
            if post_id is None:
                return Response({'error': 'postID required'}, status=status.HTTP_400_BAD_REQUEST)
            post = Posts.objects.get(postID=post_id)
            post.delete()
            return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except ValueError:
            return Response({'error': 'Invalid postID'}, status=status.HTTP_400_BAD_REQUEST)
        except Posts.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_followers(request: rest_framework.request.Request):
    try:
        post_id = int(request.query_params.get('postID'))
        if post_id is None:
            return Response({'error': 'postID required'}, status=status.HTTP_400_BAD_REQUEST)
        followers = PostFollowers.objects.filter(postID=post_id)
        follower_list = []
        for follower in followers:
            follower_list.append(follower.userID)
        return Response({'followers': follower_list}, status=status.HTTP_200_OK)
    except ValueError:
        return Response({'error': 'Invalid postID'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
