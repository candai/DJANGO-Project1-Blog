from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default= datetime.now, blank=True) 

# DONT FORGET TO 1-MAKEMIGRATIONS AND 2-MIGRATE
# In order to make this Post visible in /admin, register it in posts.admin.py!!!! <-- IMPORTANT