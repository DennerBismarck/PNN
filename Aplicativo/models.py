from django.db import models

# Create your models here.
class Estado(models.Model):
    est_id = models.AutoField(primary_key=True)
    est_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.est_estado

class Cidade(models.Model):
    cid_id = models.AutoField(primary_key=True)
    cid_cidade = models.CharField(max_length=50)
    cid_est_id = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.cid_cidade

class Profissao(models.Model):
    pro_id = models.AutoField(primary_key=True)
    pro_profissao = models.CharField(max_length=100)

    def __str__(self):
        return self.pro_profissao

    class Meta:
        verbose_name        = "Profissão"
        verbose_name_plural = "Profissões"

class Situacao(models.Model):
    sit_id = models.AutoField(primary_key=True)
    sit_situacao = models.CharField(max_length=100)

    def __str__(self):
        return self.sit_situacao

    class Meta:
        verbose_name        = "Situação"
        verbose_name_plural = "Situações"

class Genero(models.Model):
    gen_id = models.AutoField(primary_key=True)
    gen_generos = models.CharField(max_length=20)

    def __str__(self):
        return self.gen_generos

    class Meta:
        verbose_name        = "Gênero"

class Necessitado(models.Model):
    nec_id          = models.AutoField(primary_key=True)
    nec_nome        = models.CharField(max_length=100)
    nec_idade       = models.IntegerField(default=0)
    nec_logradouro  = models.CharField(max_length=100)
    nec_cpf         = models.CharField(max_length=14)

    nec_sit_id      = models.ForeignKey(Situacao, on_delete=models.CASCADE, default=1)
    nec_pro_id      = models.ForeignKey(Profissao, on_delete=models.CASCADE, default=1)
    nec_gen_id      = models.ForeignKey(Genero, on_delete=models.CASCADE, default=1)
    nec_cid_id      = models.ForeignKey(Cidade, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nec_nome

    class Meta:
        verbose_name        = "Necessitado"