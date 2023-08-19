from django.test import TestCase
from django.contrib.auth.models import User
from datasets.models import Dataset
from analysis.models import Analysis

class AnalysisModelTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )

        # Create a sample dataset
        self.dataset = Dataset.objects.create(
            user=self.user,
            dataset_name="Test Dataset",
            dataset_description="Description",
            filetype="CSV",
            processed=False,
            data_locator="http://example.com/dataset.csv"
        )

        # Create a sample analysis
        self.analysis = Analysis.objects.create(
            user=self.user,
            dataset=self.dataset,
            types='EXPLORE',
            cost=100.50,
            resources={"resource1": "value1", "resource2": "value2"},
            completed=False
        )

    def test_analysis_creation(self):
        self.assertEqual(self.analysis.user, self.user)
        self.assertEqual(self.analysis.dataset, self.dataset)
        self.assertEqual(self.analysis.types, 'EXPLORE')
        self.assertEqual(self.analysis.cost, 100.50)
        self.assertEqual(self.analysis.resources, {
            "resource1": "value1", 
            "resource2": "value2"
        })
        self.assertEqual(self.analysis.completed, False)

    def test_analysis_string_representation(self):
        self.assertEqual(str(self.analysis), f"Analysis {self.analysis.id} - EXPLORE")

    def test_analysis_update(self):
        self.analysis.cost = 150.75
        self.analysis.save()
        self.analysis.refresh_from_db()
        self.assertEqual(self.analysis.cost, 150.75)

    def test_analysis_delete(self):
        self.analysis.delete()
        with self.assertRaises(Analysis.DoesNotExist):
            Analysis.objects.get(pk=self.analysis.id)
