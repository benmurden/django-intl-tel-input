import json

from django import forms
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class IntlTelInputWidget(forms.TextInput):
    input_type = 'tel'

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/'
                '12.4.0/css/intlTelInput.css',
                ),
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/'
            '12.4.0/js/intlTelInput.min.js',
            'intl_tel_input/init.js',
            )

    def __init__(self, attrs=None, allow_dropdown=True,
                 preferred_countries=['us', 'gb'], default_code='us',
                 auto_geo_ip=False):
        final_attrs = {'size': '2'}
        if attrs is not None:
            final_attrs.update(attrs)

        self.js_attrs = {
            'size': '20',
            'placeholder': final_attrs.pop('placeholder', None),
            'data-allow-dropdown': allow_dropdown,
            'data-preferred-countries': json.dumps(preferred_countries),
            'data-default-code': default_code,
            'data-auto-geo-ip': auto_geo_ip,
        }

        super(IntlTelInputWidget, self).__init__(attrs=final_attrs)

    def build_attrs(self, extra_attrs=None, **kwargs):
        "Helper function for building an attribute dictionary."
        attrs = dict(self.attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    def render(self, name, value, renderer=None, attrs=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, name=name, size=2)
        final_attrs['type'] = 'hidden'
        if value != '':
            final_attrs['value'] = force_text(self._format_value(value))

        self.js_attrs['class'] = ' '.join([
            'intl-tel-input', final_attrs.get('class', '')
            ]).strip()

        output = [format_html('<input{}>', flatatt(final_attrs))]
        select = self.render_select()
        output.append(select)
        return mark_safe('\n'.join(output))

    def render_select(self):
        output = format_html('<input{}>', flatatt(self.js_attrs))
        return output
