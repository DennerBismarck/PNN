from django.contrib import admin
from Aplicativo     import models

# Modelos Gerais
admin.site.register(models.Estado)
admin.site.register(models.Cidade)
admin.site.register(models.Profissao)
admin.site.register(models.Situacao)
admin.site.register(models.Genero)
# Modelos de Necessitados
admin.site.register(models.Necessitado)
admin.site.register(models.Atualizacao)
# Modelos de ONG
admin.site.register(models.ONG)
admin.site.register(models.TEL_DAS_ONGS)
admin.site.register(models.EMAIL_DAS_ONGS)