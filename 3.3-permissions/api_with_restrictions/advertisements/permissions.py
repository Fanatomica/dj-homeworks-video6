from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

from rest_framework import permissions

from advertisements.models import Advertisement

from django.db.models import Q

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        admins = User.objects.filter(is_staff=True)
        if request.user in admins:
            return True
        elif request.user == obj.creator:
            return True
        return False

class IsOwnerDraft(BasePermission):
    def has_permission(self, request, view):
        if request.user.pk is None:
            view.queryset = Advertisement.objects.filter(draft=False)
        else:
            view.queryset = Advertisement.objects.filter(Q(creator=request.user) | Q(draft=False))
        return True
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and not obj.draft:
            return True
        return obj.draft and obj.creator == request.user

