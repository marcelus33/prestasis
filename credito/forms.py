import datetime

import django.forms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.core.validators import RegexValidator

from base.models import Vendedor, Cliente
from credito.models import Credito, Pago, Comision, Cuota


class CreditoForm(forms.ModelForm):
    cliente_search = forms.CharField(label="Cliente", max_length=128, required=True)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Credito
        fields = ['fecha_alta', 'numero', 'cliente', 'cliente_search', 'cuotero', 'vendedor']

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_alta'].widget.attrs.update({
            'class': 'datepicker form-control',
            'autocomplete': 'off'
        })
        if self.instance.id:
            cliente = self.instance.cliente
            cliente_initial = "{} - {}".format(cliente.nombre, cliente.ci)
            self.fields['cliente_search'].initial = cliente_initial
        else:
            last_id = Credito.objects.all().last().id
            self.fields['numero'].initial = last_id + 1
        self.fields['vendedor'].label = "Oficial"
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class CreditoVendedorForm(forms.ModelForm):
    cliente_search = forms.CharField(label="Cliente", max_length=128, required=True)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Credito
        fields = ['cliente', 'cliente_search', 'cuotero', 'vendedor']

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        queryset = Vendedor.objects.filter(usuario=user)
        self.fields['vendedor'].queryset = queryset
        self.fields['vendedor'].initial = queryset.first()
        self.fields['vendedor'].label = "Oficial"
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))
        self.helper.add_input(
            Button('button', 'Agregar cliente', data_toggle="modal", data_target="#modal-cliente", css_id='add-cliente',
                   css_class='btn-success'))


class CreditoDesembolsarForm(forms.ModelForm):
    fecha_desembolso = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Credito
        fields = ('fecha_desembolso', )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_desembolso'].required = True
        self.fields['fecha_desembolso'].widget.attrs.update({
            'class': 'datepicker form-control',
            'autocomplete': 'off'
        })
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))

    def clean(self):
        cleaned_data = self.cleaned_data
        fecha_desembolso = self.data.get('fecha_desembolso')
        fecha_desembolso = datetime.datetime.strptime(fecha_desembolso, "%d/%m/%Y").date()
        fecha_aprobacion = self.instance.fecha_aprobacion
        if fecha_aprobacion > fecha_desembolso:
            msg = "La fecha de desembolso no puede ser menor a la fecha de aprobación ({}).".format(
                fecha_aprobacion.strftime("%d/%m/%Y"))
            self.add_error('fecha_desembolso', msg)
        return cleaned_data


class PagoForm(forms.ModelForm):
    cuota = forms.ModelChoiceField(queryset=Cuota.objects.none())
    cliente_search = forms.CharField(label="Cliente", max_length=128, required=False)
    monto = forms.CharField(max_length=24,
                            validators=[RegexValidator("^\d+(\.\d+)*$", message="Sólo puede ingresar números.")])

    class Meta:
        model = Pago
        fields = '__all__'

    field_order = ['cliente_search', 'fecha', 'cuota', 'monto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].initial = datetime.datetime.now()
        self.fields['fecha'].widget.attrs.update({
            'class': 'datepicker form-control',
            'autocomplete': 'off'
        })
        self.fields['monto'].widget.attrs.update({
            'class': 'auto-numeric form-control',
        })
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class ComisionForm(forms.ModelForm):

    class Meta:
        model = Comision
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class ClienteModalForm(forms.ModelForm):
    ci = forms.CharField(max_length=16,
                         validators=[RegexValidator("^[0-9]*$", message="Sólo puede ingresar números.")])

    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget.attrs.update({
            'class': 'datepicker form-control',
            'autocomplete': 'off'
        })
        self.fields['fecha_nacimiento'].help_text = "Formato: dd/mm/YYYY"
        self.helper = FormHelper()
        self.helper.add_input(Button('button', 'Guardar', css_class='btn-primary'))
