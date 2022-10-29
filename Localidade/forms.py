from Localidade     import models
from django.forms   import ModelForm

class CidadeForm(ModelForm):
    class Meta:
        model = models.Cidade
        fields = [
            'cid_cidade',
            'cid_est_id',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cid_cidade'].widget.attrs.update({'class': 'form-label'})
        self.fields['cid_est_id'].widget.attrs.update({'class': 'form-label'})