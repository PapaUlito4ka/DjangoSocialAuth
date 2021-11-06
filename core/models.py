from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=4, null=False)
    send_at = models.DateTimeField(auto_now_add=True)

