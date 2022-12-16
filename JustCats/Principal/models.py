from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class UserManager(BaseUserManager):
    def create_user(self, email,username=None, password=None,photo=None,staff=False,admin=False, activo=True,):
        user = self.model(
            email=self.normalize_email(email),  
            username=username,
            photo=photo,
            
        )
        user.set_password(password)
        user.admin = admin
        user.staff = staff
        user.activo = activo
        user.save()
        return user

    def create_superuser(self, email,username, password):
        user = self.create_user(
            email,username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save()
        return user
class Usuario(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='',
        max_length=60,
        unique=True,
    )
    username = models.CharField(
        verbose_name='',
        max_length=24,
        unique=True,
    )
    photo = models.ImageField(
        upload_to = 'media/ImagePerfil/',
        default='media/ImagePerfil/userImageDefault.png',
        verbose_name='',
        max_length=40,
        unique=False,
    )
    activo = models.BooleanField(default=True)
    admin = models.BooleanField(default=False) 
    staff = models.BooleanField(default=False) 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "El usuario tiene un permiso especifico?"
        return True

    def has_module_perms(self, app_label):
        "El usuario tiene permisos para ver la aplicacion 'app_label'?"
        return True
    @property
    def is_admin(self):
        "El usuario es un administrador?"
        return self.admin
    @property
    def is_staff(self):
        "El usuario es un administrador?"
        return self.staff
    objects = UserManager()