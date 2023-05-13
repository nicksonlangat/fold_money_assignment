from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Define a custom user manager
class UserAccountManager(UserManager):
    # override create user method to accept email as username
    def create_user(self, email=None, password=None, **extra_fields):
        return super().create_user(
            email,
            email=email,
            password=password,
            **extra_fields
        )

    # override createsuperuser method to accept email as username
    def create_superuser(self, email=None, password=None, **extra_fields):
        return super().create_superuser(
            email,
            email=email,
            password=password,
            **extra_fields
        )


# define our custom user model
class UserAccount(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'


    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    class Meta:
        ordering = ['-date_joined']

