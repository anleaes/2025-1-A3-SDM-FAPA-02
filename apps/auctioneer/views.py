from django.shortcuts import render
from .models import Auctioneer
from rest_framework import viewsets
from .serializer import AuctioneerSerializer

# Create your views here.

class AuctioneerViewSet(viewsets.ModelViewSet):
    queryset = Auctioneer.objects.all()
    serializer_class = AuctioneerSerializer  