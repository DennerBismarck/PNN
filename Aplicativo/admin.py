from django.contrib import admin
from Aplicativo     import models

# Register your models here.
admin.site.register(models.Estado)
admin.site.register(models.Cidade)
admin.site.register(models.Profissao)
admin.site.register(models.Situacao)
admin.site.register(models.Genero)
admin.site.register(models.Usuario)
admin.site.register(models.TEL_DOS_USU)
admin.site.register(models.EMAIL_DOS_USU)
admin.site.register(models.Necessitado)
admin.site.register(models.Atualizacao)