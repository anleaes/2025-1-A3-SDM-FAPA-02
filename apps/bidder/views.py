from django.shortcuts import render
from .models import Bidder
from rest_framework import viewsets
from .serializer import BidderSerializer

# Create your views here.

class BidderViewSet(viewsets.ModelViewSet):
    queryset = Bidder.objects.all()
    serializer_class = BidderSerializer 