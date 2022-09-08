from django.db import models

# Create your models here.
class Profissao(models.Model):
    pro_id = models.AutoField(primary_key=True)
    pro_profissao = models.CharField(max_length=100)

    def __str__(self):
        return self.pro_profissao

class Situacao(models.Model):
    sit_id = models.AutoField(primary_key=True)
    sit_situacao = models.CharField(max_length=100)

    def __str__(self):
        return self.sit_situacao

class Genero(models.Model):
    gen_id = models.AutoField(primary_key=True)
    gen_generos = models.CharField(max_length=20)

    def __str__(self):
        return self.gen_generos

class Necessitado(models.Model):
    nec_id          = models.AutoField(primary_key=True)
    nec_nome        = models.CharField(max_length=100)
    nec_idade       = models.IntegerField(default=0)
    nec_logradouro  = models.CharField(max_length=100)
    nec_cpf         = models.CharField(max_length=14)

    nec_sit_id      = models.ForeignKey(Situacao, on_delete=models.CASCADE, default=1)
    nec_pro_id      = models.ForeignKey(Profissao, on_delete=models.CASCADE, default=1)
    nec_gen_id      = models.ForeignKey(Genero, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nec_nome