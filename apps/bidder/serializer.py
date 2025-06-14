from .models import Bidder
from rest_framework import serializers

class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidder
        fields = '__all__'