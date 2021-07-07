from django.contrib.auth.models import (
    AbstractBaseUser
)
from django.db import models

from common.models.crud_timestamps_mixin import CRUDTimestampsMixin
from core.managers import UserManager


class User(CRUDTimestampsMixin, AbstractBaseUser):
    USERNAME_FIELD = 'email'

    objects = UserManager()

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)

    """
    An admin who is normal staff
    """
    is_staff = models.BooleanField(default=False)

    """
    An admin who is a superuser
    """
    is_superuser = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        default_permissions = ()
        ordering = ('id',)
