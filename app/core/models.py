"""
Database models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manages all the users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ User in the System """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class About(models.Model):
    """ About section """
    content = models.TextField()
    skills = models.JSONField(default=list)
    color_text = models.JSONField(default=list)
    colors = models.JSONField(default=list)

    def __str__(self):
        """Returns the string representation of the model"""
        return self.content[:50]


class Blogs(models.Model):
    """Blog section"""
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

