import rest_framework.request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from job.models import Jobs
from job.serializers import JobSerializer


@api_view(['GET'])
def get_jobs(request: rest_framework.request.Request):
    job_id = request.query_params.get('fieldID')
    if job_id is None:
        return Response({'error': 'Missing required parameter'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        job_id = int(job_id)
    except ValueError:
        return Response({'error': 'Invalid fieldID'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        jobs = Jobs.objects.filter(fieldID=job_id).order_by('jobID')
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
