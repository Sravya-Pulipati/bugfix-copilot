from django.db import models

class BugLog(models.Model):
    raw_log = models.TextField()
    parsed_error = models.TextField()
    ai_analysis = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.parsed_error
    
severity = models.CharField(max_length=10, default="LOW")