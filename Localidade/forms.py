from Localidade     import models
from django.forms   import ModelForm, Widget

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