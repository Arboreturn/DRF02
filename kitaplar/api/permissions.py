from rest_framework import permissions
from pprint import pprint
from rest_framework.permissions import SAFE_METHODS

# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request,view)
        return request.method in permissions.SAFE_METHODS or is_admin # safe methodlara uyuyor mu yoksa admin mi diye bakıyor.
    


class IsYorumSahibiOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return  request.method == obj.yorum_sahibi