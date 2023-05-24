from django.db import models

# Create your models here.

class UserRole(models.Model):
    role_id=models.CharField(max_length=100)
    role_name= models.CharField(max_length=100)
    description= models.TextField()

    # def __str__(self):
    #     return self.username



    