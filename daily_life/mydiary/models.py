from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.



class Diary(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default='Title...')
    content = models.TextField(default='Content...')
    added_date =  models.DateTimeField(('Date-Time'),default=datetime.datetime.now)

    def __str__(self):
        return self.title