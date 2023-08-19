from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Dataset
        fields = [
            'id', 'user', 'dataset_name', 'dataset_description', 
            'date_created', 'date_modified', 'filetype', 'processed', 'data_locator'
        ]
