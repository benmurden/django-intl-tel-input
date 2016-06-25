import json
from django import forms


class IntlTelInputWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/css/intlTelInput.css',),
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/js/intlTelInput.min.js',)

    def __init__(self, attrs=None, use_utils=True):
        final_attrs = {'class': 'phone-field', 'type': 'tel', 'size': '20'}
        if attrs is not None:
            final_attrs.update(attrs)

        self.options = {}
        if use_utils:
            self.options['utilsScript'] = 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/js/utils.js'

        super(IntlTelInputWidget, self).__init__(attrs=final_attrs)

    def render(self, name, value, attrs=None):
        output_html = super(IntlTelInputWidget, self).render(name, value, attrs=attrs)
        output_html += format_html('<script>$("#{}").intlTelInput({});</script>', self._id, self.get_options())
        return output_html

    def get_options(self):
        return json.dumps(self.options)
