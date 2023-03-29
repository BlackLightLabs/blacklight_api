from rest_framework import serializers

from .models import BlacklightNeuralNetworkRun


class BlacklightRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlacklightNeuralNetworkRun
        fields = '__all__'
