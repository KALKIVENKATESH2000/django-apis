from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    employe_id = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    ph_num = models.BigIntegerField()
    
    def __str__(self):
        return self.name
    
    