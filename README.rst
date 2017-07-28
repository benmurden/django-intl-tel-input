django-intl-tel-input
=====================

.. image:: https://travis-ci.org/benmurden/django-intl-tel-input.svg?branch=master
    :target: https://travis-ci.org/benmurden/django-intl-tel-input
.. image:: https://codecov.io/gh/benmurden/django-intl-tel-input/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/benmurden/django-intl-tel-input

A Django form widget based on the jQuery plugin `intl-tel-input`_.

This is a new package, so it doesn't implement all the features of
intl-tel-input. However, it has been stable in testing, so if you're
still down...

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

Include ``{{ form.media.css }}`` in the ``<head>`` of your template. This will ensure all styles are parsed before the widget is displayed.

If you have included jQuery at the end of your document, then don't
forget to update the template where this widget appears with a
``{{ form.media.js }}``. Put it in a block that allows it to come after
jQuery.

If you're using `crispy-forms`_, the static content will be inserted automatically beside the input. To prevent this, be sure to set ``include_media = False`` on your form helper.

.. code:: python

    class MyForm(forms.Form):
    ...
        def __init__(self, *args, **kwargs):
            self.helper = FormHelper()
            self.helper.include_media = False
    ...

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

The widget can be invoked with keyword arguments which translate to the options
available in intl-tel-input.

allow_dropdown
  Shows the country dropdown.
  Default: True
