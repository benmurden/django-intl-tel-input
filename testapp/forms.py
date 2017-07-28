from django import forms

from intl_tel_input.widgets import IntlTelInputWidget


class TelForm(forms.Form):
    tel_number = forms.CharField(widget=IntlTelInputWidget())


class TelFormAttrs(forms.Form):
    tel_number = forms.CharField(widget=IntlTelInputWidget(
        attrs={'size': 10, 'title': 'Telephone number'}
        ))
