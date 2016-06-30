# django-intl-tel-input
A Django form widget based on the jQuery plugin [intl-tel-input](https://github.com/jackocnr/intl-tel-input).

This is a new package, so it doesn't implement all the features of intl-tel-input. However, it has been stable in testing, so if you're still down...

## Installation
Install straight from the repo.
```
pip install -e git://github.com/benmurden/django-intl-tel-input.git#egg=django-intl-tel-input
```

Add intl-tel-input to your INSTALLED_APPS, so Django can find the init script.
```
...
INSTALLED_APPS += ('intl_tel_input',)
...
```

## Usage
Simply add `IntlTelInputWidget` to your form field.
```
from intl_tel_input.widgets import IntlTelInputWidget

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['foo', 'bar']
        widgets = {
            'bar': IntlTelInputWidget()
        }
...
```

If you have included jQuery at the end of your document, then don't forget to update the template when this widget appears with a `{{ form.media.js }}`. Put it in a block that allows it to come after jQuery.
