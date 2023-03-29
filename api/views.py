from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import BlacklightRunSerializer
from .models import BlacklightNeuralNetworkRun
from .tasks import fit_neural_network
from django.http import FileResponse
from django.shortcuts import get_object_or_404
import os


class BlacklightRunViewSet(viewsets.ModelViewSet):
    queryset = BlacklightNeuralNetworkRun.objects.all()
    serializer_class = BlacklightRunSerializer

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        return get_object_or_404(queryset, pk=pk)

    @action(detail=True, methods=['post'])
    def fit(self, request, pk=None):
        nn = self.get_object()
        X_train = request.data.get('X_train')
        y_train = request.data.get('y_train')
        X_test = request.data.get('X_test')
        y_test = request.data.get('y_test')
        options = request.data.get('options')

        fit_neural_network.delay(nn.id, X_train, y_train, X_test, y_test, options)

        return Response({'status': 'fitting in progress'})

    @action(detail=True, methods=['get'])
    def download_model(self, request, pk=None):
        nn = self.get_object()

        if nn.status != "completed":
            return Response({'status': 'Model is not ready'})

        if not nn.model_path:
            return Response({'status': 'Model file not found'})

        response = FileResponse(open(nn.model_path, 'rb'), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(nn.model_path)}"'
        return response
