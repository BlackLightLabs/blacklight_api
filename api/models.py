from django.db import models


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
