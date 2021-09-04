from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, is_customer=False, is_employee=False, password=None):
        if not email:
            raise ValueError('Users must have an phone number')

        user = self.model(
            email=self.normalize_email(email),
            is_customer=is_customer,
            is_employee=is_employee,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, is_customer, is_employee, password):
        user = self.create_user(
            email,
            password=password,
            is_customer=is_customer,
            is_employee=is_employee,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_customer', 'is_employee']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
