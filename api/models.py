from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlacklightNeuralNetworkRun(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='pending')
    model_path = models.CharField(max_length=255, blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Datasets(models.Model): 
    """Model representing a dataset."""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='pending')
    file_path = models.CharField(max_length=255, blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class Analysis(models.Model): 
    """Model representing a specific analysis that is run on a dataset."""
    id = models.AutoField(primary_key=True)
    dataset_id = models.ForeignKey(Datasets, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    analysis_type = models.CharField(max_length=200)
    flags = models.CharField(max_length=200)
    def __str__(self):
        return self.name



