from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)    # beacause one user can have only 1 profile
    photo = models.ImageField(default='profilepictures/profilepic.jpg',upload_to='profilepictures')  

    def __str__(self):
        return self.user.username