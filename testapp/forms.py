from django import forms

from intl_tel_input.widgets import IntlTelInputWidget


class TelForm(forms.Form):
    tel_number = forms.CharField(widget=IntlTelInputWidget())
