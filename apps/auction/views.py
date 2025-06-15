from django.shortcuts import render
from .models import Auction
from rest_framework import viewsets
from .serializer import AuctionSerializer
# Create your views here.

class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer  