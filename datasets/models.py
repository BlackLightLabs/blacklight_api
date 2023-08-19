from django.db import models
from django.contrib.auth.models import User

class Dataset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dataset_name = models.CharField(max_length=255)
    dataset_description = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    filetype = models.CharField(max_length=100)
    processed = models.BooleanField(default=bool(False))
    data_locator = models.URLField()  # URLField might be best for storing URLs

    def __str__(self):
        return self.dataset_name
