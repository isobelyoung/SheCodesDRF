from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # always accepts these arguments, inbuilt function for all objects
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner==request.user
        
class IsSupporterOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # always accepts these arguments, inbuilt function for all objects
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter==request.user