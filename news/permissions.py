from rest_framework import permissions

class IsNewsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.moderator == request.user
