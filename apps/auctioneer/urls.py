from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'auctioneer'

router = routers.DefaultRouter()
router.register('', views.AuctioneerViewSet, basename='leiloeiro')

urlpatterns = [
    path('', include(router.urls) )
]
