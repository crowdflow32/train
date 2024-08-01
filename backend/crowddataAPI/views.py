import os
import uuid
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from .video_processing import process_video

@api_view(['POST'])
def upload_video(request):
    file = request.FILES.get('video_file')
    if not file:
        return Response({'error': 'No video file provided'}, status=status.HTTP_400_BAD_REQUEST)

    video_id = str(uuid.uuid4())
    video = Video.objects.create(
        video_id=video_id,
        video_file=file
    )
    return Response(VideoSerializer(video).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def process_video_view(request):
    video_id = request.data.get('video_id')
    try:
        video = Video.objects.get(video_id=video_id)
    except Video.DoesNotExist:
        return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)

    if video.processed:
        return Response({'status': 'Already processed'}, status=status.HTTP_200_OK)

    video_path = os.path.join(settings.MEDIA_ROOT, video.video_file.name)
    results = process_video(video_path)  # Process the video with your ML model
    video.results = results
    video.processed = True
    video.save()

    return Response({'status': 'Processing completed', 'video_id': video_id}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_results(request, video_id):
    try:
        video = Video.objects.get(video_id=video_id)
    except Video.DoesNotExist:
        return Response({'status': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)

    if not video.processed:
        return Response({'status': 'Processing pending'}, status=status.HTTP_202_ACCEPTED)

    return Response({'status': 'Completed', 'results': video.results}, status=status.HTTP_200_OK)