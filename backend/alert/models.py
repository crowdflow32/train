from django.db import models

class Alert(models.Model):
    ALERT_TYPES = [
        ('OVER', 'Overcrowding'),
        ('SEC', 'Security Issue'),
        ('MAINT', 'Maintenance'),
    ]

    alert_type = models.CharField(max_length=10, choices=ALERT_TYPES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alert_type}: {self.message}"
