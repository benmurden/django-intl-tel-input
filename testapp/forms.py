from django import forms

from intl_tel_input.widgets import IntlTelInputWidget


class TelForm(forms.Form):
    tel_number = forms.CharField(widget=IntlTelInputWidget())


class TelFormAttrs(forms.Form):
    tel_number = forms.CharField(widget=IntlTelInputWidget(
        attrs={'title': 'Telephone number'},
        preferred_countries=['jp'],
        default_code='jp'
    ))


class TwoTelForm(TelForm):
    tel_number_2 = forms.CharField(widget=IntlTelInputWidget())
