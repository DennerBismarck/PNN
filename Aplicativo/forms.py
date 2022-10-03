from Aplicativo import models
from django.forms import ModelForm, Widget

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
        

class CidadeForm(ModelForm):
    class Meta:
        model = models.Cidade
        fields = [
            'cid_cidade',
            'cid_est_id',
        ]

class ProfissaoForm(ModelForm):
    class Meta:
        model = models.Profissao
        fields= [
            'pro_profissao',
        ]