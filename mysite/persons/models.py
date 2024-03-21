from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=1000,default='abc')
    nid = models.CharField(max_length=13)

    def __str__(self):
        return self.name