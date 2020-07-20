from rest_framework import permissions


class Catepermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False


class Orderpermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
