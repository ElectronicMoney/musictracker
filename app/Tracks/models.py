from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Track(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title