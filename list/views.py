from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend 

from .serializers import TaskSerializer, ListSerializer
from .models import Task, List

class ListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ListSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(user=user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(parent_list__user=user)

# Búsquedas y filtros (Django-filters)

class ListFiltersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = [DjangoFilterBackend, 
                       filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'user']
    ordering_fields = ['title', 'created', 'user']

    filterset_fields = {
    'user': ['exact'],
    'title': ['exact']
}
