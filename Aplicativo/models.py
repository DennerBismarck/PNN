from django.db import models
from Usuario.models import Usuario
from Localidade.models import Cidade

# ===================================================================
# Todos os Modelos Abaixo vão para a série de tabelas de NECESSITADOS!
# ===================================================================

class Profissao(models.Model):
    pro_id          = models.AutoField(primary_key=True)
    pro_profissao   = models.CharField(verbose_name='Profissão',max_length=100)

    def __str__(self):
        return self.pro_profissao

    class Meta:
        ordering            = ['pro_profissao']
        verbose_name        = "Profissão"
        verbose_name_plural = "Profissões"

class Situacao(models.Model):
    sit_id          = models.AutoField(primary_key=True)
    sit_situacao    = models.CharField(verbose_name='Situação',max_length=100)

    def __str__(self):
        return self.sit_situacao

    class Meta:
        verbose_name        = "Situação"
        verbose_name_plural = "Situações"

class Genero(models.Model):
    gen_id      = models.AutoField(primary_key=True)
    gen_generos = models.CharField(verbose_name='Gênero', max_length=20)

    def __str__(self):
        return self.gen_generos

    class Meta:
        verbose_name        = "Gênero"

class Necessitado(models.Model):
    nec_id          = models.AutoField(primary_key=True)
    nec_nome        = models.CharField(verbose_name="Nome",max_length=100)
    nec_idade       = models.IntegerField(verbose_name="Idade",default=0)
    nec_logradouro  = models.CharField(verbose_name="Logradouro",max_length=100)
    nec_cpf         = models.CharField(verbose_name="CPF",max_length=14)

    nec_sit_id      = models.ForeignKey(Situacao, verbose_name="Situação",on_delete=models.CASCADE, default=1)
    nec_pro_id      = models.ForeignKey(Profissao, verbose_name="Profissão",on_delete=models.CASCADE, default=1)
    nec_gen_id      = models.ForeignKey(Genero, verbose_name="Gênero",on_delete=models.CASCADE, default=1)
    nec_cid_id      = models.ForeignKey(Cidade, verbose_name="Cidade",on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nec_nome

    class Meta:
        verbose_name        = "Necessitado"

class Atualizacao(models.Model):
    att_id      = models.AutoField(primary_key=True)
    att_usu_id  = models.ForeignKey(Usuario, verbose_name="Usuário", related_name='usuario', on_delete=models.CASCADE, default=1)
    att_nec_id  = models.ForeignKey(Necessitado, verbose_name="Necessitado", related_name='necessitado', on_delete=models.CASCADE, default=1)
    att_date    = models.DateTimeField(verbose_name="Data da Atualização", auto_now_add=True)

    att_nec_nome        = models.CharField(verbose_name="Nome",max_length=100)
    att_nec_idade       = models.IntegerField(verbose_name="Idade",default=0)
    att_nec_logradouro  = models.CharField(verbose_name="Logradouro",max_length=100)
    att_nec_cpf         = models.CharField(verbose_name="CPF",max_length=14)

    att_nec_sit_id      = models.ForeignKey(Situacao, verbose_name="Situação",on_delete=models.CASCADE, default=1)
    att_nec_pro_id      = models.ForeignKey(Profissao, verbose_name="Profissão",on_delete=models.CASCADE, default=1)
    att_nec_gen_id      = models.ForeignKey(Genero, verbose_name="Gênero",on_delete=models.CASCADE, default=1)
    att_nec_cid_id      = models.ForeignKey(Cidade, verbose_name="Cidade",on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "Usuário %s atualizou %s às %s" % (self.att_usu_id, self.att_nec_id, self.att_date)

    class Meta:
        verbose_name        = "Atualização"
        verbose_name_plural = "Atualizações"
        unique_together = ['att_id', 'att_usu_id', 'att_nec_id']