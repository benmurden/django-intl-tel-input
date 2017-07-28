from django.conf.urls import url

from .views import attrs_test, home

urlpatterns = [
    url(r'^$', home),
    url(r'^attrs-test/$', attrs_test)
]
