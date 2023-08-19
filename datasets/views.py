from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
from .models import Dataset
from django.core.exceptions import ValidationError
from rest_framework.exceptions import NotFound
from .serializers import DatasetSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_datasets(request):
    try:
        # Filter datasets by the logged-in user
        datasets = Dataset.objects.filter(user=request.user)
        
        # If no datasets are found, raise a NotFound error
        if not datasets.exists():
            raise NotFound(detail="No datasets found for this user.")
        
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except NotFound as e:
        # If datasets not found for the user
        return Response({"detail": e.detail}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Handle unexpected errors
        return Response(
            {"detail": "An unexpected error occurred. Please try again."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_dataset(request):
    user = request.user
    data = request.data

    # Try to manually create the Dataset object
    try:
        dataset = Dataset(
            user=user,
            dataset_name=data.get('dataset_name'),
            dataset_description=data.get('dataset_description'),
            filetype=data.get('filetype'),
            processed=data.get('processed', False),
            data_locator=data.get('data_locator')
        )
        dataset.full_clean()  # This will validate the model fields
        dataset.save()

        # Serialize the created object
        serializer = DatasetSerializer(dataset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except ValidationError as e:
        return Response(e.message_dict, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_dataset_detail(request, dataset_id):
    try:
        dataset = Dataset.objects.get(id=dataset_id, user=request.user)
    except Dataset.DoesNotExist:
        return Response({"detail": "Dataset not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"detail": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = DatasetSerializer(dataset)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_dataset(request, dataset_id):
    dataset = get_object_or_404(Dataset, id=dataset_id, user=request.user)
    serializer = DatasetSerializer(dataset, data=request.data, partial=True)  # partial=True allows for partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_dataset(request, dataset_id):
    dataset = get_object_or_404(Dataset, id=dataset_id, user=request.user)
    dataset.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
