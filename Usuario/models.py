from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUsuarioManager(BaseUserManager):
    def create_user(self, usu_nome, password=None):
        if not usu_nome:
            raise ValueError("Insira um NOME válido!")
        Usuario = self.model(
            usu_nome = usu_nome
        )
        Usuario.set_password(password)
        Usuario.save()
        return Usuario
    
    def create_superuser(self, usu_nome, password):
        Usuario = self.create_user(
            usu_nome = usu_nome,
            password = password,
        )
        Usuario.is_admin = True
        Usuario.is_staff = True
        Usuario.is_superuser = True
        Usuario.save()
        return Usuario

class Usuario(AbstractBaseUser):
    usu_id      = models.AutoField(primary_key=True)
    usu_nome    = models.CharField(max_length=50, unique=True, verbose_name="Usuário")

    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    objects = MyUsuarioManager()

    USERNAME_FIELD = 'usu_nome'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.usu_nome

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name        = "Usuário"
        verbose_name_plural = "Usuários"

class TEL_DOS_USU(models.Model):
    tel_telefone    = models.CharField(max_length=15, primary_key=True)
    tel_usu_id      = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.tel_telefone

    class Meta:
        verbose_name        = "Telefone de Usuário"
        verbose_name_plural = "Telefone dos Usuários"
        unique_together = (("tel_telefone", "tel_usu_id"),)

class EMAIL_DOS_USU(models.Model):
    ema_email    = models.CharField(max_length=40, primary_key=True)
    ema_usu_id   = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ema_email

    class Meta:
        verbose_name        = "E-mail de Usuário"
        verbose_name_plural = "E-mail dos Usuários"
        unique_together = (("ema_email", "ema_usu_id"),)