from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MenuSerializer
from .models import MenuShow
from rest_framework.permissions import IsAuthenticated

class MenuSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MenuShow.objects.all().order_by('menu_title')
    serializer_class = MenuSerializer
