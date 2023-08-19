from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from datasets.models import Dataset
from rest_framework_simplejwt.tokens import RefreshToken

class BaseDatasetTestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a JWT token for the test user
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)

        # Authenticate the client with the token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Create a sample dataset
        self.dataset = Dataset.objects.create(
            user=self.user,
            dataset_name="Test Dataset",
            dataset_description="Description",
            filetype="CSV",
            processed=False,
            data_locator="http://example.com/dataset.csv"
        )




class TestCreateDataset(BaseDatasetTestCase):

    def test_create_dataset_happy_path(self):
        url = reverse('dataset-create')
        data = {
            'dataset_name': 'New Dataset',
            'dataset_description': 'New Description',
            'filetype': 'JSON',
            'processed': False,
            'data_locator': 'http://example.com/new_dataset.json'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the dataset is saved in the database
        dataset_exists = Dataset.objects.filter(dataset_name='New Dataset').exists()
        self.assertTrue(dataset_exists)

    def test_create_dataset_sad_path(self):
        url = reverse('dataset-create')
        data = {
            'dataset_description': 'New Description',
            'filetype': 'JSON',
            'processed': False,
            'data_locator': 'http://example.com/new_dataset.json'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that the dataset is NOT saved in the database
        dataset_exists = Dataset.objects.filter(dataset_name='New Dataset').exists()
        self.assertFalse(dataset_exists)


class TestRetrieveDataset(BaseDatasetTestCase):

    def test_get_dataset_detail(self):
        url = reverse('dataset-detail', kwargs={'dataset_id': self.dataset.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['dataset_name'], 'Test Dataset')


class TestUpdateDataset(BaseDatasetTestCase):

    def test_update_dataset(self):
        url = reverse('dataset-update', kwargs={'dataset_id': self.dataset.id})
        data = {'dataset_name': 'Updated Dataset'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.dataset.refresh_from_db()
        self.assertEqual(self.dataset.dataset_name, 'Updated Dataset')


class TestDeleteDataset(BaseDatasetTestCase):

    def test_delete_dataset(self):
        url = reverse('dataset-delete', kwargs={'dataset_id': self.dataset.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Dataset.objects.filter(id=self.dataset.id).exists())


