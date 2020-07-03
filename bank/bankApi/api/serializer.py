from bankApi.models import Bank
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['ifsc','bank_id','branch','address','city','district','state','name']
