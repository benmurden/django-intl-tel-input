django-intl-tel-input
=====================

A Django form widget based on the jQuery plugin `intl-tel-input`_.

This is a new package, so it doesn’t implement all the features of
intl-tel-input. However, it has been stable in testing, so if you’re
still down…

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

Simply add ``IntlTelInputWidget`` to your form field.

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
        tel_number = forms.CharField(widget=IntlTelInputWidget())

    ...

Form media
----------

If you have included jQuery at the end of your document, then don’t
forget to update the template where this widget appears with a
``{{ form.media.js }}``. Put it in a block that allows it to come after
jQuery.

If you load jQuery in the head of your document, you needn't worry about
this step - widget media will be inserted right after the field. If you
want to keep all JS at the end of your document, you can still use the
``{{ form.media.js }}`` tag to achieve that. Just make sure it always comes
after the form field.

.. _intl-tel-input: https://github.com/jackocnr/intl-tel-input

Options
-------

The widget can be invoked with keyword arguments which translate to the options
available in intl-tel-input.

allow_dropdown
  Shows the country dropdown.
  Default: True
