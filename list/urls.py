from django.urls import path, include
from rest_framework import routers

from list.views import *

urlpatterns = [
    path('lists/', ListViewSet.as_view(), name = 'lists'),
    path('tasks/', TaskViewSet.as_view(), name = 'tasks'),    
]