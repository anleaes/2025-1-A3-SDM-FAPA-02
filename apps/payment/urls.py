from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'payment'

router = routers.DefaultRouter()
router.register('', views.PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls) )
]