from django.conf.urls import url

from .views import attrs_test, home, initial_test, two_fields_test

urlpatterns = [
    url(r'^$', home),
    url(r'^attrs-test/$', attrs_test),
    url(r'^initial-test/$', initial_test),
    url(r'^two-field-test/$', two_fields_test),
]
