from django.db import models
from django.contrib.auth.models import User, AbstractUser



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, blank=True, null=True)  
    profile_pic = models.ImageField(upload_to='images/', blank=True, null=True)  

    def __str__(self):
        return self.username

class Daily_task(models.Model):
    task = models.TextField()
    date = models.DateTimeField()
    compleated = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_daily_task')

    def __str__(self):
        return self.task
    
class Long_term_goals(models.Model):
    task = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    compleated = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_long_term_goals')

    def __str__(self):
        return self.task