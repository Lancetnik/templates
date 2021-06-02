from random import choice

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

 
class MyUserAccountManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')
 
        if not password:
            raise ValueError('Password must be provided')
 
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
 
        return self._create_user(email, password, **extra_fields)


def random_color():
    return choice(['#FFA133', 'red', '#FFDE33', '#4181FF', '#FFD600', 'blue', 'orange'])

 
class MyUser(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = ['full_name']
    USERNAME_FIELD = 'email'
 
    objects = MyUserAccountManager()
 
    email = models.EmailField('email', unique=True, blank=False, null=False)
    full_name = models.CharField('full name', max_length=400)
    is_staff = models.BooleanField('staff status', default=False)
    icon_color = models.CharField(max_length=20, default=random_color)

    about_me = models.TextField(null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True, max_length=200)
 
    def get_short_name(self):
        return self.email
 
    def get_full_name(self):
        return self.full_name
 
    def __unicode__(self):
        return self.email

    class Meta():
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
