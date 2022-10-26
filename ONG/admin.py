from django.contrib import admin
from ONG            import models

# Modelos de ONG
admin.site.register(models.ONG)
admin.site.register(models.TEL_DAS_ONGS)
admin.site.register(models.EMAIL_DAS_ONGS)