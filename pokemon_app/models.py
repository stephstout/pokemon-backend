from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name