from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
import uuid


class PersoUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email=email,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)

        return user


class PersoUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name="Email Adress", max_length=200, unique=True)
    username = models.CharField(
        verbose_name="username", max_length=200, unique=True)
    first_name = models.CharField(verbose_name="firstname", max_length=200)
    last_name = models.CharField(verbose_name="lastname", max_length=200)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = PersoUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_superuser(self):
        "Is the user a superuser"
        # Simplest possible answer: All admins are superusers
        return self.is_admin
