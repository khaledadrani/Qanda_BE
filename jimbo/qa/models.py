from django.db import models
from django.utils import timezone


# Create your models here.
class Problem(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    question = models.CharField(max_length=1000)
    context = models.CharField(max_length=2500)
    model_name = models.CharField(max_length=250)
    answer = models.JSONField(default=dict)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Problem({self.id},{self.question})"

    