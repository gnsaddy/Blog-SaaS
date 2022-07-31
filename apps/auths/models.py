from .managers import UserManager, FacultyManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    sid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=False,
        blank=False,
        unique=True)
    # validate with max length of 10 and min length of 10 and must be a number
    mobile = models.CharField(
        max_length=10,
        verbose_name='mobile number',
        validators=[
            MaxLengthValidator(10),
            MinLengthValidator(10),
            RegexValidator(
                regex='^[0-9]*$',
                message='Mobile number must be a number.'
            )
        ],
        null=False,
        unique=True
    )
    admin = models.BooleanField(default=False, null=True)
    faculty = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return str(f"Name: {self.first_name} {self.last_name}, Email: {self.email}")

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_faculty(self):
        return self.faculty

    @property
    def is_staff(self):
        return self.staff


# faculty user class for faculty users
class FacultyUserModel(CustomUser):

    expertise = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Expertise")
    designation = models.CharField(
        max_length=100, null=True, verbose_name="Designation")
    experience = models.CharField(
        max_length=100, null=True, verbose_name="Experience")

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['expertise']

    objects = FacultyManager()

    def __str__(self):
        return str(f"Name: {self.first_name} {self.last_name}, Email: {self.email}")

    class Meta:
        db_table = "faculty_user"
