from django.db import models

class Username(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name
