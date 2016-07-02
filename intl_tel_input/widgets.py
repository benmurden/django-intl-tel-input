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

    def __init__(self, attrs=None, use_utils=True, allow_dropdown=True):
        final_attrs = {'class': 'intl-tel-input', 'size': '20'}
        if attrs is not None:
            final_attrs.update(attrs)

        if use_utils:
            final_attrs['data-utils-script'] = True

        final_attrs['data-allow-dropdown'] = allow_dropdown

        super(IntlTelInputWidget, self).__init__(attrs=final_attrs)

    def get_options(self):
        return json.dumps(self.options)
