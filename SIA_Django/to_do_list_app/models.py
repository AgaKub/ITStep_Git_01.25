from django.db import models
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
