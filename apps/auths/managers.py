from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, mobile, password, is_active=True, is_superuser=False,
                    is_faculty=False, is_staff=False, **extra_fields):
        """
        Create and save a User with the given mobile and password.
        """
        if not mobile:
            raise ValueError(_('The given mobile must be set'))
        mobile = mobile
        user = self.model(mobile=mobile, **extra_fields)
        user.admin = is_superuser
        user.faculty = is_faculty
        user.active = is_active
        user.staff = is_staff
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mobile, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_faculty', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_faculty') is not True:
            raise ValueError(_('Superuser must have is_faculty=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(mobile, password, **extra_fields)

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser


class FacultyManager(BaseUserManager):
    def create_user(self, mobile, password, is_active=True, is_superuser=False,
                    is_faculty=True, is_staff=False, **extra_fields):
        if not mobile:
            raise ValueError(_('The given mobile must be set'))
        mobile = mobile
        user = self.model(mobile=mobile, **extra_fields)
        user.admin = is_superuser
        user.faculty = is_faculty
        user.active = is_active
        user.staff = is_staff

        # set is_faculty to True
        user.faculty = True
        if not extra_fields.get('is_faculty'):
            raise ValueError(_('Faculty user must have is_faculty=True.'))

        user.set_password(password)
        user.save()

        return user
