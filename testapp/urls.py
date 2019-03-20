from django.conf.urls import url

from .views import (attrs_test, home, initial_test, no_init_test,
                    two_fields_test)

urlpatterns = [
    url(r'^$', home),
    url(r'^attrs-test/$', attrs_test),
    url(r'^initial-test/$', initial_test),
    url(r'^two-field-test/$', two_fields_test),
    url(r'^no-init-test/$', no_init_test)
]
