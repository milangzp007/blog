from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100,default="milan")
    content = models.CharField(max_length=1000,default="milan")
    created_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    message = models.CharField(max_length=1000,default="milan")
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.message