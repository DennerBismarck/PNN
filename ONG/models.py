from django.db import models
from Localidade.models import Cidade

# ===================================================================
# Todos os Modelos Abaixo vão para a série de tabelas de ONGS!
# ===================================================================

class ONG(models.Model):
    ong_id          = models.AutoField(primary_key=True)
    ong_nome        = models.CharField(verbose_name="Nome da ONG",max_length=100)
    ong_site        = models.CharField(verbose_name="Site da ONG",max_length=70)
    ong_logradouro  = models.CharField(verbose_name="Logradouro da ONG",max_length=50)
    ong_cid_id      = models.ForeignKey(Cidade, verbose_name="Cidade da ONG",on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ong_nome

    class Meta:
        verbose_name        = "ONG"
    
class EMAIL_DAS_ONGS(models.Model):
    emo_email = models.CharField(max_length=40, primary_key=True)
    emo_ong_id = models.ForeignKey(ONG, verbose_name="ONG",on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.emo_email

    class Meta:
        verbose_name        = "E-mail da ONG"
        verbose_name_plural = "E-mail das ONGs"
        unique_together = (("emo_email", "emo_ong_id"),)

class TEL_DAS_ONGS(models.Model):
    ton_telefone = models.CharField(max_length=15, primary_key=True)
    ton_ong_id = models.ForeignKey(ONG, verbose_name="ONG",on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ton_telefone

    class Meta:
        verbose_name        = "Telefone da ONG"
        verbose_name_plural = "Telefone das ONGs"
        unique_together = (("ton_telefone", "ton_ong_id"),)
