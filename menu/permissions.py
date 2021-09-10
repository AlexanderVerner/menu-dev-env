from django.conf import settings
from rest_framework.permissions import BasePermission

class CheckKeyAuth(BasePermission):
    def has_permission(self, request, view):
        api_key_secret = request.META.get('HTTP_AUTHORIZATION')
        return api_key_secret == settings.API_TOKEN