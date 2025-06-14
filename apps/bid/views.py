from django.shortcuts import render
from .models import Bid
from rest_framework import viewsets
from .serializer import BidSerializer
# Create your views here.

class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer  