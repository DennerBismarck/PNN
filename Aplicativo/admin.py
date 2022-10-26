from django.contrib import admin
from Aplicativo     import models

# Modelos Gerais
admin.site.register(models.Profissao)
admin.site.register(models.Situacao)
admin.site.register(models.Genero)
# Modelos de Necessitados
admin.site.register(models.Necessitado)
admin.site.register(models.Atualizacao)
