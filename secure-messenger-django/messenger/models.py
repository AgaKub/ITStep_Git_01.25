from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    encrypted_message = models.TextField()
    encrypted_key = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
