from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=20)
    date=models.DateTimeField()
    text=models.TextField()
    img=models.ImageField(upload_to='events_image/')