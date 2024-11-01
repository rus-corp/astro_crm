from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
  USER_ROLE = (
    ('MN', 'Менеджер'),
    ('AD', 'Админ'),
  )
    
  email = models.EmailField(max_length=40, verbose_name='Email', unique=True)
  role = models.CharField(max_length=2, choices=USER_ROLE, blank=True)
  is_staff = models.BooleanField(default=False)
  REQUIRED_FIELDS = []
  USERNAME_FIELD = 'email'
  
  objects = CustomUserManager()
  
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'
  
  
  def __str__(self):
    return self.email