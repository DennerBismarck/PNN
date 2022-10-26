from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from . import models

# Modelos de Usuário
class UsuarioAdmin(UserAdmin):
    list_display = ('usu_nome','usu_id', 'is_admin','is_active','is_staff','is_superuser')
    search_fields = ('usu_nome','usu_id')
    ordering= ('usu_nome','usu_id', 'is_admin','is_active','is_staff','is_superuser')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (None, {
        'fields': ('usu_nome', 'password','is_admin','is_active','is_staff','is_superuser'),
    }),
    add_fieldsets = (None, {
        'fields': ('usu_nome', 'password','is_admin','is_active','is_staff','is_superuser'),
    }),

admin.site.register(models.Usuario, UsuarioAdmin)
admin.site.register(models.TEL_DOS_USU)
admin.site.register(models.EMAIL_DOS_USU)