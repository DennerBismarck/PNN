from Usuario     import models
from django.forms   import ModelForm

class EmailUserForm(ModelForm):
    class Meta:
        model = models.EMAIL_DOS_USU
        fields = [
            'ema_email'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ema_email'].widget.attrs.update(        {'class': 'form-control'})

class TelUserForm(ModelForm):
    class Meta:
        model = models.TEL_DOS_USU
        fields = [
            'tel_telefone'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tel_telefone'].widget.attrs.update(        {'class': 'form-control  format_field_tel'})