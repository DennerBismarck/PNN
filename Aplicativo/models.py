from django.db import models

# ===================================================================
# Todos os Modelos Abaixo vão para a série de tabelas de GERAIS!
# ===================================================================

class Estado(models.Model):
    est_id      = models.AutoField(primary_key=True)
    est_estado  = models.CharField(max_length=50)

    def __str__(self):
        return self.est_estado

class Cidade(models.Model):
    cid_id      = models.AutoField(primary_key=True)
    cid_cidade  = models.CharField(max_length=50)
    cid_est_id  = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.cid_cidade

# ===================================================================
# Todos os Modelos Abaixo vão para a série de tabelas de NECESSITADOS!
# ===================================================================

class Profissao(models.Model):
    pro_id          = models.AutoField(primary_key=True)
    pro_profissao   = models.CharField(max_length=100)

    def __str__(self):
        return self.pro_profissao

    class Meta:
        verbose_name        = "Profissão"
        verbose_name_plural = "Profissões"

class Situacao(models.Model):
    sit_id          = models.AutoField(primary_key=True)
    sit_situacao    = models.CharField(max_length=100)

    def __str__(self):
        return self.sit_situacao

    class Meta:
        verbose_name        = "Situação"
        verbose_name_plural = "Situações"

class Genero(models.Model):
    gen_id      = models.AutoField(primary_key=True)
    gen_generos = models.CharField(max_length=20)

    def __str__(self):
        return self.gen_generos

    class Meta:
        verbose_name        = "Gênero"

class Usuario(models.Model):
    usu_id      = models.AutoField(primary_key=True)
    usu_nome    = models.CharField(max_length=50)

    def __str__(self):
        return self.usu_nome

class TEL_DOS_USU(models.Model):
    tel_telefone    = models.CharField(max_length=15, primary_key=True)
    tel_usu_id      = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.tel_telefone

    class Meta:
        verbose_name        = "Telefone de Usuário"
        verbose_name_plural = "Telefone dos Usuários"
        unique_together = (("tel_telefone", "tel_usu_id"),)

class EMAIL_DOS_USU(models.Model):
    ema_email    = models.CharField(max_length=40, primary_key=True)
    ema_usu_id   = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ema_email

    class Meta:
        verbose_name        = "E-mail de Usuário"
        verbose_name_plural = "E-mail dos Usuários"
        unique_together = (("ema_email", "ema_usu_id"),)

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

class Atualizacao(models.Model):
    att_id      = models.AutoField(primary_key=True)
    att_usu_id  = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    att_nec_id  = models.ForeignKey(Necessitado, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "Atualização %s pelo usuário(a) %s para o necessitado(a) %s" % (self.att_id, self.att_usu_id, self.att_nec_id)

    class Meta:
        verbose_name        = "Atualização"
        verbose_name_plural = "Atualizações"
        unique_together = (("att_id", "att_usu_id", "att_nec_id"),)

# ===================================================================
# Todos os Modelos Abaixo vão para a série de tabelas de ONGS!
# ===================================================================

class ONG(models.Model):
    ong_id          = models.AutoField(primary_key=True)
    ong_nome        = models.CharField(max_length=100)
    ong_site        = models.CharField(max_length=70)
    ong_logradouro  = models.CharField(max_length=50)
    ong_cid_id      = models.ForeignKey(Cidade, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ong_nome

    class Meta:
        verbose_name        = "ONG"
    
class EMAIL_DAS_ONGS(models.Model):
    emo_email = models.CharField(max_length=40, primary_key=True)
    emo_ong_id = models.ForeignKey(ONG, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.emo_email

    class Meta:
        verbose_name        = "E-mail da ONG"
        verbose_name_plural = "E-mail das ONGs"
        unique_together = (("emo_email", "emo_ong_id"),)

class TEL_DAS_ONGS(models.Model):
    ton_telefone = models.CharField(max_length=15, primary_key=True)
    ton_ong_id = models.ForeignKey(ONG, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.ton_telefone

    class Meta:
        verbose_name        = "Telefone da ONG"
        verbose_name_plural = "Telefone das ONGs"
        unique_together = (("ton_telefone", "ton_ong_id"),)
