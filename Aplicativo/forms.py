from Aplicativo     import models
from django.forms   import ModelForm, Widget

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nec_sit_id'].widget.attrs.update({'class': 'select_id_control'})
        self.fields['nec_pro_id'].widget.attrs.update({'class': 'select_id_control'})
        self.fields['nec_gen_id'].widget.attrs.update({'class': 'select_id_control'})
        self.fields['nec_cid_id'].widget.attrs.update({'class': 'select_id_control'})


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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['att_nec_id'].widget.attrs.update({'class': 'select_id_control'})
        self.fields['att_usu_id'].widget.attrs.update({'class': 'select_id_control'})
        self.fields['att_nec_sit_id'].widget.attrs.update({'class': 'select_id_control'})
        self.fields['att_nec_pro_id'].widget.attrs.update({'class': 'select_id_control'})
        self.fields['att_nec_gen_id'].widget.attrs.update({'class': 'select_id_control'})
        self.fields['att_nec_cid_id'].widget.attrs.update({'class': 'select_id_control'})

class SituacaoForm(ModelForm):
    class Meta:
        model = models.Situacao
        fields = [
            'sit_situacao',
        ]

class ProfissaoForm(ModelForm):
    class Meta:
        model = models.Profissao
        fields= [
            'pro_profissao',
        ]

