from rest_framework.permissions import BasePermission


class IsCarOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_created == request.user


# class IsStaff(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_staff
