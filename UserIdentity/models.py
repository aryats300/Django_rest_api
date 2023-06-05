from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True) 
    role_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.role_name



class AssignRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role.role_name}"

    