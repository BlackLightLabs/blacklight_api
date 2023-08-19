from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.reverse import reverse
from rest_framework import status
from django.contrib.auth.models import User
from datasets.models import Dataset
from analysis.models import Analysis

class BaseAnalysisTestCase(APITestCase):
    
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        # Create a JWT token for the test user
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        # Authenticate the client with the token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Authenticate the test client
        self.client.login(username='testuser', password='testpassword')

        # Create a sample dataset
        self.dataset = Dataset.objects.create(
            user=self.user,
            dataset_name="Test Dataset",
            dataset_description="Description",
            filetype="CSV",
            processed=False,
            data_locator="http://example.com/dataset.csv"
        )

class TestListAnalyses(BaseAnalysisTestCase):

    def setUp(self):
        super().setUp()

        # Create a sample analysis
        Analysis.objects.create(
            user=self.user,
            dataset=self.dataset,
            types='EXPLORE',
            cost=100.50,
            resources={"resource1": "value1", "resource2": "value2"},
            completed=False
        )

    def test_list_analyses_happy_path(self):
        url = reverse('analyses-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_analyses_sad_path(self):
        url = reverse('analyses-list')
        self.client.logout()  # unauthenticated request
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class TestCreateAnalysis(BaseAnalysisTestCase):
    def test_create_analysis_happy_path(self):
        url = reverse('analysis-create')
        data = {
            'dataset': self.dataset.id,
            'types': 'RECOMMEND',
            'cost': 100,
            'resources': {"resource": "value"},
            'completed': True
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Analysis.objects.filter(id=response.data['id']).exists())

    def test_create_analysis_sad_path(self):
        url = reverse('analysis-create')
        data = {
            # Missing required fields
        }
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TestAnalysisDetail(BaseAnalysisTestCase):

    def setUp(self):
        super().setUp()

        # Create a sample analysis
        self.analysis = Analysis.objects.create(
            user=self.user,
            dataset=self.dataset,
            types='EXPLORE',
            cost=100.50,
            resources={"resource1": "value1", "resource2": "value2"},
            completed=False
        )

    def test_get_analysis_detail_happy_path(self):
        url = reverse('analysis-detail', kwargs={'analysis_id': self.analysis.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.analysis.id)

    # non-existent analysis ID
    def test_get_analysis_detail_sad_path(self):
        url = reverse('analysis-detail', kwargs={'analysis_id': 9999})          
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_analysis_detail_happy_path(self):
        url = reverse('analysis-detail', kwargs={'analysis_id': self.analysis.id})
        data = {
            'types': 'EXTRACT'
        }
        response = self.client.put(url, data)
        
        self.analysis.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.analysis.types, 'EXTRACT')

    def test_update_analysis_detail_sad_path(self):
        url = reverse('analysis-detail', kwargs={'analysis_id': self.analysis.id})
        data = {
            'types': 'INVALID_TYPE'
        }
        response = self.client.put(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_analysis_detail_happy_path(self):
        url = reverse('analysis-detail', kwargs={'analysis_id': self.analysis.id})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse
