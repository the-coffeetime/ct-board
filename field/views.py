import rest_framework.request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from field.models import Fields
from field.serializers import FieldSerializer


@api_view(['GET'])
def get_field(request: rest_framework.request.Request):
    if not request.query_params:
        try:
            fields = Fields.objects.all().order_by('fieldID')
            serializer = FieldSerializer(fields, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    field_id = request.query_params.get('fieldID')
    if field_id is None:
        return Response({'error': 'Missing required parameter'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        field_id = int(field_id)
    except ValueError:
        return Response({'error': 'Invalid fieldID'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        field = Fields.objects.get(fieldID=field_id)
        serializer = FieldSerializer(field)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Fields.DoesNotExist:
        return Response({'error': 'Field not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
