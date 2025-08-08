from django.db import models
from django.contrib.auth.models import User

class Daily_task(models.Model):
    task = models.TextField()
    date = models.DateTimeField()
    compleated = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_daily_task')

    def __str__(self):
        return self.task
    
class Long_term_goals(models.Model):
    task = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    compleated = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_long_term_goals')

    def __str__(self):
        return self.task