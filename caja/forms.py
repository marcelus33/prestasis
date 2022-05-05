import django.forms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from caja.models import MovimientoCaja, ConceptoMovimiento


class MovimientoCajaForm(forms.ModelForm):
    class Meta:
        model = MovimientoCaja
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))


class ConceptoMovimientoForm(forms.ModelForm):
    class Meta:
        model = ConceptoMovimiento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))
