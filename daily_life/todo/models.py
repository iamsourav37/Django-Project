from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.



class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=200,default='')
    added_date = models.DateTimeField(('Date-Time'),default=datetime.datetime.now)

    def __str__(self):
        return self.text
