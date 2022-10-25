from Aplicativo     import models
from Usuario.models import Usuario, TEL_DOS_USU, EMAIL_DOS_USU
from django.forms   import ModelForm, Widget

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields= [
            'usu_nome',
            'password',
        ]

class UsuEmaForm(ModelForm):
    class Meta:
        model = EMAIL_DOS_USU
        fields = [
            'ema_email',
            'ema_usu_id',
        ]

class UsoTelForm(ModelForm):
    class Meta:
        model = TEL_DOS_USU
        fields = [
            'tel_telefone',
            'tel_usu_id',
        ]

class NecessitadoForm(ModelForm):
    class Meta:
        model = models.Necessitado
        fields = [
            'nec_nome',
            'nec_idade',
            'nec_logradouro',
            'nec_cpf',
            'nec_sit_id',
            'nec_pro_id',
            'nec_gen_id',
            'nec_cid_id',
        ]

class AtualizacaoForm(ModelForm):
    class Meta:
        model = models.Atualizacao
        fields = [
            'att_nec_id',
            'att_usu_id',
            'att_nec_nome',
            'att_nec_idade',
            'att_nec_logradouro',
            'att_nec_cpf',
            'att_nec_sit_id',
            'att_nec_pro_id',
            'att_nec_gen_id',
            'att_nec_cid_id',
        ]

class ONGForm(ModelForm):
    class Meta:
        model = models.ONG
        fields = [
            'ong_nome',
            'ong_site',
            'ong_logradouro',
            'ong_cid_id',
        ]

class SituacaoForm(ModelForm):
    class Meta:
        model = models.Situacao
        fields = [
            'sit_situacao',
        ]

class CidadeForm(ModelForm):
    class Meta:
        model = models.Cidade
        fields = [
            'cid_cidade',
            'cid_est_id',
        ]

class EstadoForm(ModelForm):
    class Meta:
        model = models.Estado
        fields = [
            'est_estado',
        ]

class ProfissaoForm(ModelForm):
    class Meta:
        model = models.Profissao
        fields= [
            'pro_profissao',
        ]

