from django.db import models

# Create your models here.

class Issue(models.Model):
    PRIORITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM","Medium"),
        ("HIGH", "High"),
    ]
    STATUS_CHOICES = [
        ("OPEN","Open"),
        ("IN_PROGRESS","In Progress"),
        ("RESOLVED", "Resolved"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=200)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="MEDIUM"
    )

    status = models.CharField(
        max_length=20 ,
        choices= STATUS_CHOICES,
        default="OPEN"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    