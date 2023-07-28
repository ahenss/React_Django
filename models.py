from django.db import models

# Create your models here.
# users/models.py

class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.URLField()

    def __str__(self):
        return self.first_name + " " + self.last_name
