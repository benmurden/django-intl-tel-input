import json
from django import forms
from django.utils.html import format_html


class IntlTelInputWidget(forms.TextInput):
    input_type = 'tel'

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/css/intlTelInput.css',),
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/js/intlTelInput.min.js', 'intl_tel_input/init.js')

    def __init__(self, attrs=None, allow_dropdown=True, preferred_countries=['us', 'gb']):
        final_attrs = {'class': 'intl-tel-input', 'size': '20'}
        if attrs is not None:
            final_attrs.update(attrs)

        final_attrs['data-allow-dropdown'] = allow_dropdown
        final_attrs['data-preferred-countries'] = json.dumps(preferred_countries)

        super(IntlTelInputWidget, self).__init__(attrs=final_attrs)

    def get_options(self):
        return json.dumps(self.options)
