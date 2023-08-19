from django.db import models
from django.contrib.auth.models import User
from datasets.models import Dataset

class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    TYPE_CHOICES = [
        ('EXPLORE', 'Explore'),
        ('RECOMMEND', 'Recommend'),
        ('EXTRACT', 'Extract'),
    ]
    types = models.CharField(max_length=10, choices=TYPE_CHOICES)
    cost = models.FloatField()
    resources = models.JSONField(blank=True, null=True)    
    completed = models.BooleanField(default=False)
    def __str__(self):
        return f"Analysis {self.id} - {self.types}"

