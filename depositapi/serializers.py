from .models import Deposit  
from rest_framework import serializers

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'