from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    video_file = models.FileField(upload_to='videos/')
    processed = models.BooleanField(default=False)
    results = models.JSONField(null=True, blank=True)