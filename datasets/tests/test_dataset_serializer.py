from django.test import TestCase
from django.contrib.auth.models import User
from datasets.models import Dataset
from datasets.serializers import DatasetSerializer

class DatasetSerializerTestCase(TestCase):

    def setUp(self):
        # Create a user and dataset for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.dataset = Dataset.objects.create(
            user=self.user,
            dataset_name="Test Dataset",
            dataset_description="This is a test dataset.",
            filetype="CSV",
            processed=False,
            data_locator="https://example.com/test-dataset.csv"
        )

    def test_serializer_data(self):
        # Serialize the dataset
        serializer = DatasetSerializer(self.dataset)
        
        # Check that the serialized data matches our expectations
        self.assertEqual(serializer.data['user'], str(self.user))
        self.assertEqual(serializer.data['dataset_name'], "Test Dataset")
        self.assertEqual(serializer.data['dataset_description'], "This is a test dataset.")
        self.assertEqual(serializer.data['filetype'], "CSV")
        self.assertFalse(serializer.data['processed'])
        self.assertEqual(serializer.data['data_locator'], "https://example.com/test-dataset.csv")
        # ... you can continue this for all fields

    def test_serializer_validity(self):
        # Sample data to validate
        data = {
            'user': self.user.id,
            'dataset_name': "Another Test Dataset",
            'dataset_description': "Description for another test dataset.",
            'filetype': "JSON",
            'processed': True,
            'data_locator': "https://example.com/another-test-dataset.json"
        }

        # Validate the data
        serializer = DatasetSerializer(data=data)
        self.assertTrue(serializer.is_valid())
