import rest_framework.request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from board.models import Boards, BoardFollowers
from board.serializers import BoardSerializer


class BoardDetailView(APIView):
    def get(self, request: rest_framework.request.Request):
        field_id = request.query_params.get('fieldID')
        job_id = request.query_params.get('jobID')

        if field_id is not None:
            try:
                field_id = int(field_id)
            except ValueError:
                return Response({'error': 'Invalid fieldID'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                boards = Boards.objects.filter(fieldID=field_id).order_by('boardID')
                serializer = BoardSerializer(boards, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif job_id is not None:
            try:
                job_id = int(job_id)
            except ValueError:
                return Response({'error': 'Invalid jobID'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                boards = Boards.objects.filter(jobID=job_id).order_by('boardID')
                serializer = BoardSerializer(boards, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'Missing required parameter'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_followers(request: rest_framework.request.Request):
    board_id = request.query_params.get('boardID')

    if board_id is None:
        return Response({'error': 'Missing required parameter'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        board_id = int(board_id)
    except ValueError:
        return Response({'error': 'Invalid boardID'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        followers = BoardFollowers.objects.filter(postID=board_id)
        return Response(followers, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
