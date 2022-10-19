from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Modelos de Usuário
class UsuarioAdmin(UserAdmin):
    list_display = ('usu_nome','usu_id', 'is_admin','is_active','is_staff','is_superuser')
    search_fields = ('usu_nome','usu_id')
    readonly_fields = ('is_admin','is_active','is_staff','is_superuser')
    ordering= ('usu_nome','usu_id', 'is_admin','is_active','is_staff','is_superuser')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# admin.site.register(models.Usuario, UsuarioAdmin)
# admin.site.register(models.TEL_DOS_USU)
# admin.site.register(models.EMAIL_DOS_USU)