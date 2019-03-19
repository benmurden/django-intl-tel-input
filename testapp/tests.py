from __future__ import unicode_literals

from time import sleep

import html5lib
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
        self.assertIn(
            '/js/intlTelInput-jquery.min.js',
            r.content.decode('utf-8')
        )
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
        self.assertIn('placeholder="foobar"', r.content.decode('utf-8'))

    def test_with_initial(self):
        r = self.client.get('/initial-test/')
        self.assertIn('value="+81123456789"', r.content.decode('utf-8'))


class wait_for_utils_script(object):
    def __call__(self, driver):
        return driver.execute_script("return window.intlTelInputUtils !== undefined")


class AcceptanceTest(StaticLiveServerTestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = Firefox(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_two_inputs(self):
        driver = self.driver
        driver.get('{live_server_url}/two-field-test/'.format(
            live_server_url=self.live_server_url
        ))
        WebDriverWait(driver, 5).until(
            wait_for_utils_script()
        )
        inputs = driver.find_elements_by_css_selector('input.intl-tel-input')
        inputs[0].send_keys('555-5555')
        inputs[1].send_keys('555-4444')
        inputs[1].send_keys(Keys.RETURN)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'success-text'))
        )

        self.assertIn('Form is valid', driver.page_source)
