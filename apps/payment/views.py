from django.shortcuts import render
from .models import Payment
from rest_framework import viewsets
from .serializer import PaymentSerializer
# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer 