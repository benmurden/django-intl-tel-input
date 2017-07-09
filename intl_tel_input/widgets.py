import json
import copy

from django import forms
from django.utils.safestring import mark_safe
from django.forms.renderers import get_default_renderer


class IntlTelInput(forms.TextInput):
    input_type = 'tel'

    def __init__(self, attrs=None, **kwargs):
        my_attrs = {'size': '20', 'class': 'js-intl-tel-input'}

        # Add class which is used to identify intl-tel-input
        if attrs is not None:
            my_attrs['class'] = ' '.join([my_attrs['class'], attrs.pop('class', '')]).strip()

        # Add intl-tel-input options as data attributes.
        # All data attribute values will be available in init.js via the jQuery data() function using camelCase,
        # e.g. 'data-allow-dropdown' > data.allowDropdown
        my_attrs['data-allow-dropdown'] = kwargs.get('allow_dropdown', True)
        my_attrs['data-preferred-countries'] = json.dumps(kwargs.get('preferred_countries', ['us', 'gb']))
        my_attrs['data-default-code'] = kwargs.get('default_code', 'us')
        my_attrs['data-auto-geo-ip'] = kwargs.get('auto_geo_ip', False)

        if attrs is not None:
            my_attrs.update(attrs)

        super(IntlTelInput, self).__init__(my_attrs)


class IntlTelInputHidden(forms.HiddenInput):
    def __init__(self, attrs=None):
        my_attrs = {'class': 'js-intl-tel-input-hidden'}

        # Add class which is used to identify intl-tel-input
        if attrs is not None:
            my_attrs['class'] = ' '.join([my_attrs['class'], attrs.pop('class', '')]).strip()

        if attrs is not None:
            my_attrs.update(attrs)

        super(IntlTelInputHidden, self).__init__(my_attrs)


class IntlTelInputWidget(forms.Widget):
    _visible_input_key = 'visible_input'
    _hidden_input_key = 'hidden_input'

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.1.1/css/intlTelInput.css',),
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.1.1/js/intlTelInput.min.js',
            'intl_tel_input/init.js',
        )

    def __init__(self, visible_input_attrs=None, hidden_input_attrs=None, **kwargs):
        self.widgets = {
            self._visible_input_key: IntlTelInput(attrs=visible_input_attrs, **kwargs),
            self._hidden_input_key: IntlTelInputHidden(attrs=hidden_input_attrs),
        }
        super(IntlTelInputWidget, self).__init__()

    def __deepcopy__(self, memo):
        obj = copy.copy(self)
        obj.attrs = self.attrs.copy()
        obj.widgets = self.widgets.copy()
        memo[id(self)] = obj
        return obj

    def render(self, name, value, attrs=None, renderer=None):
        visible_input = self.widgets[self._visible_input_key]
        hidden_input = self.widgets[self._hidden_input_key]

        output = [
            self._render(visible_input.template_name,
                         visible_input.get_context(name, value, attrs),
                         renderer),
            self._render(hidden_input.template_name,
                         hidden_input.get_context(name, value, attrs),
                         renderer),
        ]

        return mark_safe('\n'.join(output))

    def _render(self, template_name, context, renderer=None):
        if renderer is None:
            renderer = get_default_renderer()
        return renderer.render(template_name, context)
