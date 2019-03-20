import json

from django import forms
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe

INTL_TEL_INPUT_VERSION = '15.0.1'


class IntlTelInputWidget(forms.TextInput):
    input_type = 'tel'

    def __init__(self, attrs=None, allow_dropdown=True,
                 preferred_countries=['us', 'gb'], default_code='us',
                 use_default_init=True):

        self.use_default_init = use_default_init

        final_attrs = {
            'size': '20',
            'data-allow-dropdown': allow_dropdown,
            'data-preferred-countries': json.dumps(preferred_countries),
            'data-default-code': default_code,
        }

        if attrs is not None:
            final_attrs.update(attrs)

        super(IntlTelInputWidget, self).__init__(attrs=final_attrs)

    @property
    def media(self):
        js = (
                'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/'
                '{version}/js/intlTelInput-jquery.min.js'.format(
                    version=INTL_TEL_INPUT_VERSION
                ),
            )

        if self.use_default_init:
            js += ('intl_tel_input/init.js',)

        return forms.Media(
            css={
                'all': (
                    'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/'
                    '{version}/css/intlTelInput.css'.format(
                        version=INTL_TEL_INPUT_VERSION
                    ),
                ),
            },
            js=js
        )

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
