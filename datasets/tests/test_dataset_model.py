from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from datasets.models import Dataset


class DatasetModelTestCase(TestCase):

    def setUp(self):
        # Create a user to be used in the Dataset model
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )

    def test_dataset_creation(self):
        # Create a Dataset
        dataset = Dataset.objects.create(
            user=self.user,
            dataset_name="Test Dataset",
            dataset_description="This is a test dataset.",
            date_created=date.today(),
            date_modified=date.today(),
            filetype="CSV",
            processed=False,
            data_locator="https://example.com/test-dataset.csv"
        )

        # Check if the dataset was saved properly
        self.assertEqual(Dataset.objects.count(), 1)
        
        # Validate attributes
        self.assertEqual(dataset.dataset_name, "Test Dataset")
        self.assertEqual(dataset.user, self.user)
        self.assertEqual(dataset.dataset_description, "This is a test dataset.")
        self.assertEqual(dataset.date_created, date.today())
        self.assertEqual(dataset.date_modified, date.today())
        self.assertEqual(dataset.filetype, "CSV")
        self.assertFalse(dataset.processed)
        self.assertEqual(dataset.data_locator, "https://example.com/test-dataset.csv")
