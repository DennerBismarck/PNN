from django.contrib import admin
from Aplicativo     import models

# Register your models here.
admin.site.register(models.Estado)
admin.site.register(models.Cidade)
admin.site.register(models.Profissao)
admin.site.register(models.Situacao)
admin.site.register(models.Genero)
admin.site.register(models.Necessitado)