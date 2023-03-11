from django.db import models
from django.shortcuts import get_object_or_404
# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=100)
    des=models.TextField(null=True,blank=True)
    no_of_likes=models.IntegerField(default=0,blank=True)
    active=models.BooleanField(default=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    @classmethod
    def get_all_posts(cls):
        return cls.objects.all()
    
    @classmethod
    def get_post(cls,id):
        return get_object_or_404(cls, pk=id)
