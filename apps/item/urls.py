from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'item'

router = routers.DefaultRouter()
router.register('', views.ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls) )
]