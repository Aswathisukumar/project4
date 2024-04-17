from django.db import models

# Create your models here.
class people(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    photo=models.FileField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name
