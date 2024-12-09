

from rest_framework import serializers
from pesaapp.models import mpesaRequest, MpesaPayments

class mpesaRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = mpesaRequest
        fields = '__all__'

class MpesaPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPayments
        fields = '__all__'