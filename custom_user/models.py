""""Models for custom user app."""
from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.db import models


class User(BaseUser):
    """Custom user model that uses email as username."""
    objects = BaseUserManager()


class UserProfile(models.Model):
    """User profile"""