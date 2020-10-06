from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    role = models.TextField()

    def __str__(self):
        return self.name
