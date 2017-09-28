from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy

from .models import Subject


class BaseModelForm(forms.ModelForm):
    '''Extends ModelForm to add bootstrap form-control'''

    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            classes = self.fields[field].widget.attrs.get("class")
            if classes is not None:
                classes += " form-control"
            else:
                classes = "form-control"
            self.fields[field].widget.attrs.update({
                'class': classes
            })


class FirstTimeForm(forms.Form):
    first_time = forms.BooleanField(
        label='',
        widget=forms.RadioSelect(
            attrs={'class': 'custom-control-input'},
            choices=((1, "SÍ"), (0, "NO"))),
        initial=1, required=False)


class SubjectForm(BaseModelForm):
    class Meta:
        model = Subject
        fields = ['code', 'age', 'sex',
                  'life_satisfaction', 'civil_status',
                  'last_studies', 'occupation',
                  'home_country', 'home_city',
                  'current_country', 'current_city',
                  'postal_code']
        labels = {'code': 'Código',
                  'age': 'Edad', 'sex': 'Sexo',
                  'life_satisfaction': 'Satisfacción vital',
                  'civil_status': 'Estado civil',
                  'last_studies': 'Últimos estudios',
                  'occupation': 'Ocupación',
                  'home_country': 'País de nacimiento',
                  'home_city': 'Ciudad de nacimiento',
                  'current_country': 'País de residencia',
                  'current_city': 'Ciudad de residencia',
                  'postal_code': 'Código postal actual'}


def validate_50(value):
    if value == 50:
        raise ValidationError(
            ugettext_lazy(
                'Mueve el cursor, no puede estar justo en el medio.'),
            params={'value': value},
        )


def slider_input():
    return forms.NumberInput(attrs={'id': 'slider',
                                    'class': 'slider',
                                    'type': 'range',
                                    'value': '50',
                                    'min': '0',
                                    'max': '100'})


class ItemForm(forms.Form):
    slider = forms.IntegerField(
        validators=[validate_50],
        label='',
        widget=slider_input())
