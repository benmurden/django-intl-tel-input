import json

from django import forms


class IntlTelInput(forms.TextInput):
    input_type = 'tel'

    def __init__(self, attrs=None, **kwargs):
        """
        Initialize visible International Telephone Input field in which users enter their phone number.

        :param attrs: Dictionary of HTML attributes, e.g. {'size': '50', 'class': 'my-css-class'}
        :param kwargs: intl-tel-input options (see :class:~.IntlTelInputWidget`)
        """
        my_attrs = {'size': '30', 'class': 'js-intl-tel-input'}

        # Add class which is used to identify intl-tel-input
        if attrs is not None:
            my_attrs['class'] = ' '.join([my_attrs['class'], attrs.pop('class', '')]).strip()

        # Add intl-tel-input options as data attributes.
        # All data attribute values will be available in init.js via the jQuery data() function using camelCase,
        # e.g. 'data-allow-dropdown' > data.allowDropdown
        my_attrs['data-allow-dropdown'] = kwargs.get('allow_dropdown', True)
        my_attrs['data-auto-hide-dial-code'] = kwargs.get('auto_hide_dial_code', True)
        my_attrs['data-auto-placeholder'] = kwargs.get('auto_placeholder', "polite")
        my_attrs['data-dropdown-container'] = kwargs.get('dropdown_container', "")
        my_attrs['data-exclude-countries'] = json.dumps(kwargs.get('exclude_countries', []))
        my_attrs['data-format-on-display'] = kwargs.get('format_on_display', True)
        my_attrs['data-auto-geo-ip'] = kwargs.get('auto_geo_ip', False)
        my_attrs['data-initial-country'] = kwargs.get('initial_country', '')
        my_attrs['data-national-mode'] = kwargs.get('national_mode', True)
        my_attrs['data-placeholder-number-type'] = kwargs.get('placeholder_number_type', "MOBILE")
        my_attrs['data-only-countries'] = json.dumps(kwargs.get('only_countries', []))
        my_attrs['data-preferred-countries'] = json.dumps(kwargs.get('preferred_countries', ['us', 'gb']))
        my_attrs['data-separate-dial-code'] = kwargs.get('separate_dial_code', False)

        if attrs is not None:
            my_attrs.update(attrs)

        super(IntlTelInput, self).__init__(my_attrs)


class IntlTelInputHidden(forms.HiddenInput):
    def __init__(self, attrs=None):
        """
        Initialize hidden International Telephone Input field which is used to store the complete international number.

        :param attrs: Dictionary of HTML attributes, e.g. {'class': 'my-class'}
        """
        my_attrs = {'class': 'js-intl-tel-input-hidden'}

        # Add class which is used to identify intl-tel-input
        if attrs is not None:
            my_attrs['class'] = ' '.join([my_attrs['class'], attrs.pop('class', '')]).strip()

        if attrs is not None:
            my_attrs.update(attrs)

        super(IntlTelInputHidden, self).__init__(my_attrs)


class IntlTelInputWidget(forms.MultiWidget):

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.1.1/css/intlTelInput.css',),
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.1.1/js/intlTelInput.min.js',
            'intl_tel_input/init.js',
        )

    def __init__(self, visible_input_attrs=None, hidden_input_attrs=None, **kwargs):
        """
        Initialize MultiWidget comprising a TextInput and a HiddenInput widget.

        :param visible_input_attrs: Dictionary with HTML attributes of the TextInput widget.
        :param hidden_input_attrs: Dictionary with HTML attributes of the HiddenInput widget.
        :param kwargs: intl-tel-input options according to
            https://github.com/jackocnr/intl-tel-input/blob/master/README.md#options.
            All options are added as data attributes (e.g. data-auto-placeholder="polite") to this input field.

            Be aware that option names must be given in snake_case. They will be translated to camelCase in the init.js.
        """
        _widgets = (
            IntlTelInput(attrs=visible_input_attrs, **kwargs),
            IntlTelInputHidden(attrs=hidden_input_attrs),
        )
        super(IntlTelInputWidget, self).__init__(_widgets)

    def decompress(self, value):
        """
        Put the phone number value which is stored in the database in a list.
        Since the visible input field gets field via jQuery, the first list element is empty and the
            second element is the stored phone number which will be printed in the hidden input field.

        :param value: The value stored in the database
        :return: List with two elements. The second element contains the phone number which will be written to
            the hidden input field.
        """
        if value:
            # Return empty value for visible field because it gets filled with jQuery based on the hidden field.
            return [None, value]
        return [None, None]

    def value_from_datadict(self, data, files, name):
        """
        Gets data from the form (visible and hidden input field) and return the value which should
         be validated and stored in the database.

        :param data: Dictionary of input data from the form.
        :param files: -
        :param name: Field name of the form, e.g. phone_number
        :return: A string representing the entered phone number as international telephone number, e.g. +436641234567
        """
        phonelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        return phonelist[1] # 1 = hidden field
