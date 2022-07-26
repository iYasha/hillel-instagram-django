from authorizations.models import User
from django.db import models


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
