from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# status r category er jonno choices create korlam jate dropdown theke select kora jai
STUTAS =[
    ('pending','Pending'),
    ('completed','Completed')
]
CATAGORY=[
    ('work','work'),
    ('home','home'),
    ('other','other'),
]

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    due_date=models.DateField()
    due_time=models.TimeField()
    status=models.CharField(max_length=10,choices=STUTAS,default='pending')
    category=models.CharField(max_length=10,choices=CATAGORY)
    is_completed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title