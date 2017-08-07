from __future__ import unicode_literals

import html5lib
from django.test import TestCase

from intl_tel_input.widgets import IntlTelInputWidget


class IntlTelInputTest(TestCase):
    def assertValidHTML(self, content, msg=None):
        parser = html5lib.HTMLParser()
        parser.parse(content)
        if parser.errors:
            default_msg = ['Content is invalid HTML:']
            lines = content.split('\n')
            for position, errorcode, datavars in parser.errors:
                default_msg.append(
                    '  %s' % html5lib.constants.E[errorcode] % datavars
                    )
                default_msg.append('    %s' % lines[position[0] - 1])

            msg = self._formatMessage(msg, '\n'.join(default_msg))
            raise self.failureException(msg)

    def test_render(self):
        r = self.client.get('/')
        self.assertValidHTML(r.content)
        self.assertEqual(r.status_code, 200)

    def test_static(self):
        r = self.client.get('/')
        self.assertIn('/js/intlTelInput.min.js', r.content.decode('utf-8'))
        self.assertIn('/intl_tel_input/init.js', r.content.decode('utf-8'))
        self.assertIn('/css/intlTelInput.css', r.content.decode('utf-8'))

    def test_post(self):
        r = self.client.post('/', {'tel_number': '+81123456789'})
        self.assertRedirects(r, '/?ok')

    def test_with_attrs(self):
        r = self.client.get('/attrs-test/')
        self.assertIn('title="Telephone number"', r.content.decode('utf-8'))
        self.assertIn('data-default-code="jp"', r.content.decode('utf-8'))
        self.assertIn('data-preferred-countries="[&quot;jp&quot;]"',
                      r.content.decode('utf-8'))

    def test_with_initial(self):
        r = self.client.get('/initial-test/')
        self.assertIn('value="+81123456789"', r.content.decode('utf-8'))

    def test_extra_attrs(self):
        widget = IntlTelInputWidget()
        attrs = widget.build_attrs(extra_attrs={'required': True})
        self.assertTrue(attrs['required'])
        attrs = widget.build_attrs()
        self.assertIsNone(attrs.get('required'))
        self.assertEqual(attrs['size'], '2')
