from django.urls import path,include
from crowddataAPI.views import *
urlpatterns = [
    path('upload-video/', upload_video, name='upload_video'),
    path('process-video/', process_video_view, name='process_video'),
    path('results/<str:video_id>/', get_results, name='get_results'),
]

