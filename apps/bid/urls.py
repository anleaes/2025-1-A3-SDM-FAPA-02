from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'bid'

router = routers.DefaultRouter()
router.register('', views.BidViewSet, basename='leilao')

urlpatterns = [
    path('', include(router.urls) )
]