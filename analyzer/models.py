from django.db import models

# Create your models here.

class BugLog(models.Model):
    raw_log = models.TextField()
    parsed_error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)