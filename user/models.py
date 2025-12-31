from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_('Email Address'), max_length=50, unique=True)
#     email_is_verified = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
