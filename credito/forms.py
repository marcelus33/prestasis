import django.forms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from credito.models import Credito, Pago, Comision


class CreditoForm(forms.ModelForm):

    class Meta:
        model = Credito
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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