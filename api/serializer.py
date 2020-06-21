from rest_framework import serializers
from database.models import *

class TRXProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRXProduct
        fields = ["mst_product","color","quantity"]
        extra_kwargs = {
            'mst_product': {'write_only': True},
            'quantity': {'write_only': True}
        }

class MSTProductSerializer(serializers.ModelSerializer):
    details = TRXProductSerializer(many=True, read_only=True)

    class Meta:
        model = MSTProduct
        fields = ["id","name","price","dimension","material","max_seats","image_url","details"]
