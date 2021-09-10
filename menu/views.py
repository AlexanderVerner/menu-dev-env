from rest_framework import viewsets
from .serializers import MenuSerializer
from .models import MenuShow
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import CheckKeyAuth

class MenuSet(viewsets.ModelViewSet):
    permission_classes = (CheckKeyAuth,)
    queryset = MenuShow.objects.all().order_by('menu_title')
    serializer_class = MenuSerializer
