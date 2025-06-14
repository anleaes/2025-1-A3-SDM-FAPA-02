from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'bidder'

router = routers.DefaultRouter()
router.register('', views.CategoryViewSet, basename='ofertante')

urlpatterns = [
    path('', include(router.urls) )
]
