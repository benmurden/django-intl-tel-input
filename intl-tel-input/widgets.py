from django import forms


class IntlTelInputWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/css/intlTelInput.css',),
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/9.0.1/js/intlTelInput.min.js',)

    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'phone-field', 'type': 'tel', 'size': '20'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(IntlTelInputWidget, self).__init__(attrs=final_attrs, format=format)
