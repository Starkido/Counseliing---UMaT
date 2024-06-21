# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
# from django.db import models
# from django.utils import timezone

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     groups = models.ManyToManyField(
#         Group,
#         related_name='customuser_set',  # Add related_name to avoid conflict
#         blank=True,
#         help_text=('The groups this user belongs to. A user will get all permissions '
#                    'granted to each of their groups.'),
#         verbose_name=('groups'),
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='customuser_set',  # Add related_name to avoid conflict
#         blank=True,
#         help_text=('Specific permissions for this user.'),
#         verbose_name=('user permissions'),
#     )

#     def __str__(self):
#         return self.email

# class Counsellor(CustomUser):
#     staff_id = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     gender = models.CharField(max_length=10)
#     year_of_experience = models.PositiveIntegerField(default=0)
#     religion = models.CharField(max_length=255)

#     def __str__(self):
#         return self.email

# class Student(CustomUser):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     gender = models.CharField(max_length=10)

#     def __str__(self):
#         return self.email


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Student(CustomUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Counsellor(CustomUser):
    staff_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    year_of_experience = models.PositiveIntegerField(default=0)
    religion = models.CharField(max_length=255)

    def __str__(self):
        return self.email