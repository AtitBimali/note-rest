from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow safe methods like GET, HEAD, OPTIONS
        return obj.user == request.user  # Check if the user is the owner of the note




class SharedOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow safe methods like GET, HEAD, OPTIONS
        if hasattr(obj, 'note'):
            return obj.note.user == request.user  # Check if the user is the owner of the associated note
        return False