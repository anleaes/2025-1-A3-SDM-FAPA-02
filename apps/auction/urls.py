from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'auction'

router = routers.DefaultRouter()
router.register('', views.AuctionViewSet, basename='leilao')

urlpatterns = [
    path('', include(router.urls) )
]
