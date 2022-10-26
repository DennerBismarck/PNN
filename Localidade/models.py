from django.db import models

# ===================================================================
# Todos os Modelos Abaixo vão para a série de tabelas de GERAIS!
# ===================================================================

class Estado(models.Model):
    est_id      = models.AutoField(primary_key=True)
    est_estado  = models.CharField(verbose_name='Estado', max_length=50)

    def __str__(self):
        return self.est_estado

class Cidade(models.Model):
    cid_id      = models.AutoField(primary_key=True)
    cid_cidade  = models.CharField(verbose_name='Cidade', max_length=50)
    cid_est_id  = models.ForeignKey(Estado, verbose_name='Estado', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.cid_cidade