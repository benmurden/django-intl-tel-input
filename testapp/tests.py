import html5lib
from django.test import TestCase


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
        self.assertIn('/js/intlTelInput.min.js', r.content)
        self.assertIn('/intl_tel_input/init.js', r.content)
        self.assertIn('/css/intlTelInput.css', r.content)

    def test_post(self):
        r = self.client.post('/', {'tel_number': '+81123456789'})
        self.assertRedirects(r, '/?ok')
