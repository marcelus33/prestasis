import datetime

import django.forms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.utils import timezone

from base.models import Vendedor, Cliente
from credito.models import Credito, Pago, Comision


class CreditoForm(forms.ModelForm):

    class Meta:
        model = Credito
        fields = '__all__'

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class CreditoVendedorForm(forms.ModelForm):

    class Meta:
        model = Credito
        fields = ['cliente', 'cuotero', 'vendedor']

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        queryset = Vendedor.objects.filter(usuario=user)
        self.fields['vendedor'].queryset = queryset
        self.fields['vendedor'].initial = queryset.first()
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


class PagoForm(forms.ModelForm):

    class Meta:
        model = Pago
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Button('button', 'Guardar', css_class='btn-primary'))
