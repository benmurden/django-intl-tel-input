import json

from django import forms
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe

INTL_TEL_INPUT_VERSION = '15.0.1'


class IntlTelInputWidget(forms.TextInput):
    input_type = 'tel'

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/'
                '{version}/css/intlTelInput.css'.format(
                    version=INTL_TEL_INPUT_VERSION
                ),
            ),
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/'
            '{version}/js/intlTelInput-jquery.min.js'.format(
                version=INTL_TEL_INPUT_VERSION
            ),
        )

    def __init__(self, attrs=None, allow_dropdown=True,
                 preferred_countries=['us', 'gb'], default_code='us',
                 use_default_init=True):

        if use_default_init:
            self.Media.js += ('intl_tel_input/init.js',)

        final_attrs = {
            'size': '20',
            'data-allow-dropdown': allow_dropdown,
            'data-preferred-countries': json.dumps(preferred_countries),
            'data-default-code': default_code,
        }

        if attrs is not None:
            final_attrs.update(attrs)

        super(IntlTelInputWidget, self).__init__(attrs=final_attrs)

    def render(self, name, value, renderer=None, attrs=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, self.attrs)
        final_attrs['data-hidden-name'] = name

        if value != '':
            final_attrs['value'] = force_text(self.format_value(value))

        final_attrs['class'] = ' '.join([
            'intl-tel-input', final_attrs.get('class', '')
        ]).strip()

        output = format_html('<input{}>', flatatt(final_attrs))
        return mark_safe(output)
