from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .models import Analysis
from .serializers import AnalysisSerializer  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_analyses(request):
    analyses = Analysis.objects.filter(user=request.user)
    serializer = AnalysisSerializer(analyses, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_analysis(request):
    user = request.user
    data = request.data
    # Try to manually create the Analysis object
    try:
        analysis = Analysis(
            user=user,
            dataset_id=data.get('dataset'),
            types=data.get('types'),
            cost=data.get('cost'),
            resources=data.get('resources', []),
            completed=data.get('completed', False)
        )
        analysis.full_clean()  # This will validate the model fields
        analysis.save()

        # Serialize the created object
        serializer = AnalysisSerializer(analysis)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except ValidationError as e:
        return Response(e.message_dict, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def analysis_detail(request, analysis_id):
    analysis = Analysis.objects.filter(id=analysis_id, user=request.user).first()
    if not analysis:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AnalysisSerializer(analysis)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AnalysisSerializer(analysis, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        analysis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
