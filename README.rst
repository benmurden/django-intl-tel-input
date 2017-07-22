django-intl-tel-input
=====================

A Django form widget based on the jQuery plugin `intl-tel-input`_.

This is a new package, so it doesn't implement all the features of
intl-tel-input. However, it has been stable in testing.

Installation
------------

Install from PyPI.

.. code:: shell

    pip install django-intl-tel-input

Add intl-tel-input to your INSTALLED\_APPS, so Django can find the init
script.

.. code:: python

    ...
    INSTALLED_APPS += ('intl_tel_input',)
    ...

Usage
-----

Simply add ``IntlTelInputWidget`` to your form field. It will add a visible text input field and a hidden input field.

.. code:: python

    from intl_tel_input.widgets import IntlTelInputWidget

    class MyForm(forms.ModelForm):
        class Meta:
            model = MyModel
            fields = ['foo', 'bar']
            widgets = {
                'bar': IntlTelInputWidget()
            }
    ...

With a standard form:

.. code:: python

    class MyForm(forms.Form):
        tel_number = forms.CharField(widget=IntlTelInputWidget(
            visible_input_attrs={
                'size': '30',
                'class': 'my-css-class',
                ...
            },
            hidden_input_attrs={
                'class': 'another-css-class',
                ...
            }
        ))
        ...

The two arguments ``visible_input_attrs`` and ``hidden_input_attrs`` can be used to add additional HTML 
attributes to the visible text input field respectively to the hidden input field. 


Form media
----------

If you have included jQuery at the end of your document, then don't
forget to update the template where this widget appears with a
``{{ form.media.js }}``. Put it in a block that allows it to come after
jQuery.

If you load jQuery in the head of your document, you needn't worry about
this step - widget media will be inserted right after the field. If you
want to keep all JS at the end of your document, you can still use the
``{{ form.media.js }}`` tag to achieve that. However, if you use `crispy-forms`_,
you need to set ``include_media = False`` in order to assure that ``init.js``
gets loaded **after** jQuery and consequently to avoid JS errors:

.. code:: python

    class MyForm(forms.Form):
        def __init__(self, *args, **kwargs):
            ...
            self.helper = FormHelper()
            self.helper.include_media = False
            ...

If you use ``self.helper.include_media = False`` in your form, you
have to add ``{{ form.media.css }}`` to your template
where this widget appears in order to load ``intlTelInput.css``.

If you need to load all JS in the head, you can make the ``init.js`` script
wait for the document to be ready with the following snippet.

.. code:: javascript

    jQuery(document).ready(
      {{ form.media.js }}
    );
    
All this assumes your form context variable is called ``form``.

.. _intl-tel-input: https://github.com/jackocnr/intl-tel-input
.. _crispy-forms: https://github.com/django-crispy-forms/django-crispy-forms

Options
-------

The widget can be invoked with most keyword arguments which translate to the `options`_
available in the jQuery plugin intl-tel-input.

allow_dropdown
  Type: ``Boolean`` Default: ``True``

  Example usage:

    .. code:: python
    
        class MyForm(forms.Form):
                tel_number = forms.CharField(widget=IntlTelInputWidget(
                    allow_dropdown=False,
                ))
                ...

auto_hide_dial_code
  Type: ``Boolean`` Default: ``True``

auto_placeholder
  Type: ``String`` Default: ``"polite"``

custom_placeholder
  This option is not implemented yet.

dropdown_container
  Type: ``String`` Default: ``""``

exclude_countries
  Type: ``List`` Default: ``[]``

  Example usage:

    .. code:: python
    
        class MyForm(forms.Form):
                tel_number = forms.CharField(widget=IntlTelInputWidget(
                    exclude_countries=['at', 'de', 'ch'],
                ))
                ...

format_on_display
  Type: ``Boolean`` Default: ``True``

auto_geo_ip
  Type: ``Boolean`` Default: ``False``

  This option represents geoIpLookup. If set to ``True``, the user's location is lookup up. 
  In order to lookup the user's location, https://freegeoip.net/json/ is used.

initial_country
  Type: ``String`` Default: ``""``

national_mode
  Type: ``Boolean`` Default: ``True``

placeholder_number_type
  Type: ``String`` Default: ``"MOBILE"``

only_countries  
  Type: ``List`` Default: ``[]``  

preferred_countries
  Type: ``List`` Default: ``['us', 'gb']``

separate_dial_code
  Type: ``Boolean`` Default: ``False``

.. _options: https://github.com/jackocnr/intl-tel-input/blob/master/README.md#options
