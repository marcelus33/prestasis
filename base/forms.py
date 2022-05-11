import django.forms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from base.models import Cuotero, ComisionMora, Cliente, Vendedor, Usuario, TipoDocumento


class CuoteroForm(forms.ModelForm):

    class Meta:
        model = Cuotero
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class ComisionMoraForm(forms.ModelForm):

    class Meta:
        model = ComisionMora
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class VendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # solo usuarios que no tengan vendedores asociados
        self.fields['usuario'].queryset = Usuario.objects.filter(vendedor__isnull=True, is_superuser=False).all()
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))

    def clean_usuario(self):
        # por haber cambiado el queryset en el init
        usuario = self.cleaned_data['usuario']
        usuario = usuario.id
        return usuario


class TipoDocumentoForm(forms.ModelForm):

    class Meta:
        model = TipoDocumento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class ClienteForm(forms.ModelForm):
    ci = forms.CharField(max_length=16,
                         validators=[RegexValidator("r'^[0-9]+$", message="Sólo puede ingresar números.")])

    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'groups', 'is_active', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class ImportadorClienteForm(forms.Form):
    documento = forms.FileField(label="Documento", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Importar', css_class='btn-primary'))

