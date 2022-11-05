from ONG            import models
from django.forms   import ModelForm, Widget

class ONGForm(ModelForm):
    class Meta:
        model = models.ONG
        fields = [
            'ong_nome',
            'ong_site',
            'ong_logradouro',
            'ong_cid_id',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ong_nome'].widget.attrs.update(        {'class': 'form-control'})
        self.fields['ong_site'].widget.attrs.update(        {'class': 'form-control'})
        self.fields['ong_logradouro'].widget.attrs.update(  {'class': 'form-control'})
        self.fields['ong_cid_id'].widget.attrs.update(      {'class': 'form-control'})

class EmailONGForm(ModelForm):
    class Meta:
        model = models.EMAIL_DAS_ONGS
        fields = ['emo_email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['emo_email'].widget.attrs.update(        {'class': 'form-control'})

class TelONGForm(ModelForm):
    class Meta:
        model = models.TEL_DAS_ONGS
        fields = ['ton_telefone']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ton_telefone'].widget.attrs.update(        {'class': 'form-control'})