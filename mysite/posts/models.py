from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    # but here one user can have multiple posts
    image = models.ImageField(upload_to='images')
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True)
    date = models.DateField(auto_now_add=True)  # so we are bu default date to current date
    
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):                       # we are overwritting save method to generate slug
        if not self.slug:                                # if current object does not have a slug
            self.slug = slugify(self.title)              # then generate slug from title
        super().save(*args,**kwargs)                     # and then save that slug
        
    
    
