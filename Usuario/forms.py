from Usuario.models import Usuario, TEL_DOS_USU, EMAIL_DOS_USU
from django.forms   import ModelForm, Widget

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields= [
            'usu_nome',
            'password',
            'is_admin',
            'is_active',
            'is_superuser',
            'is_staff',
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