from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit only their own profile"""
    
