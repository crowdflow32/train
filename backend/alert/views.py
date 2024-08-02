from rest_framework import viewsets
from .models import Alert
from .serializer import AlertSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer