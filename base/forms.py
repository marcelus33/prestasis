import django.forms as forms
from django.contrib.gis import forms as gis_forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models import Q

from base.helpers import parse_string_number
from base.models import Cuotero, ComisionMora, Cliente, Vendedor, Usuario, TipoDocumento


class CuoteroForm(forms.ModelForm):
    monto = forms.CharField(max_length=24,
                            validators=[RegexValidator("^\d+(\.\d+)*$", message="Sólo puede ingresar números.")])
    pagare = forms.CharField(max_length=24,
                             validators=[RegexValidator("^\d+(\.\d+)*$", message="Sólo puede ingresar números.")])
    monto_cuota = forms.CharField(max_length=24, required=False)  # , disabled=True

    SEMANAL = 7
    QUINCENAL = 14
    MENSUAL = 30
    TIPOS_PLAZOS = (
        (SEMANAL, "Semanal"),
        (QUINCENAL, "Quincenal"),
        (MENSUAL, "Mensual"),
    )

    class Meta:
        model = Cuotero
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_plazo'] = forms.ChoiceField(choices=self.TIPOS_PLAZOS)
        for field in ['monto', 'pagare', 'monto_cuota']:
            self.fields[field].widget.attrs.update({
                'class': 'auto-numeric form-control',
            })
        self.fields['monto_cuota'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))

    def clean_monto(self):
        monto = self.cleaned_data['monto']
        return parse_string_number(monto)

    def clean_pagare(self):
        pagare = self.cleaned_data['pagare']
        return parse_string_number(pagare)

    def clean(self):
        data = self.cleaned_data
        monto = data.get("monto")
        pagare = data.get("pagare")

        if monto > pagare:
            self.add_error("pagare", "Monto del Pagaré no puede ser menor al préstamo.")
        return data


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
        query = Q(vendedor__isnull=True, is_superuser=False)
        if self.instance.id:
            query = Q(vendedor__isnull=True, is_superuser=False) | Q(vendedor=self.instance)
        self.fields['usuario'].queryset = Usuario.objects.filter(query).all()
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))

    def clean_usuario(self):
        # por haber cambiado el queryset en el init
        usuario = self.cleaned_data['usuario']
        usuario = usuario.id if usuario else None
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
                         validators=[RegexValidator("^[0-9]*$", message="Sólo puede ingresar números.")])
    latitud_ubicacion = forms.CharField(widget=forms.HiddenInput())
    longitud_ubicacion = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Cliente
        fields = ['nombre', 'tipo_documento', 'ci', 'direccion', 'telefono', 'fecha_nacimiento', 'latitud_ubicacion',
                  'longitud_ubicacion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget.attrs.update({
            'class': 'datepicker form-control',
            'autocomplete': 'off'
        })
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'is_active', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'is_active', 'is_superuser']

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
