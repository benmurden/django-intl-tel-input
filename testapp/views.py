from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TelForm, TelFormAttrs, TwoTelForm


def home(request):
    if request.POST:
        form = TelForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('{path}?ok'.format(path=request.path))
    else:
        form = TelForm()

    return render(request, 'home.html', {'form': form})


def attrs_test(request):
    form = TelFormAttrs()
    return render(request, 'home.html', {'form': form})


def initial_test(request):
    form = TelForm(initial={'tel_number': '+81123456789'})
    return render(request, 'home.html', {'form': form})


def two_fields_test(request):
    if request.POST:
        form = TwoTelForm(request.POST)
    else:
        form = TwoTelForm()
    return render(request, 'home.html', {'form': form})
