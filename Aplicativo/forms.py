from .models import Necessitado
from django.forms import ModelForm

class NecessitadoForm(ModelForm):
    class Meta:
        model = Necessitado
        fields = [
            'nec_nome',
            'nec_idade',
            'nec_logradouro',
            'nec_cpf',
            'nec_sit_id',
            'nec_pro_id',
            'nec_gen_id',
            'nec_cid_id'
        ]