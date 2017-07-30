from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TelForm, TelFormAttrs


def home(request):
    if request.POST:
        form = TelForm(request.POST)
        return HttpResponseRedirect(request.path + '?ok')
    else:
        form = TelForm()

    return render(request, 'home.html', {'form': form})


def attrs_test(request):
    form = TelFormAttrs()
    return render(request, 'home.html', {'form': form})


def initial_test(request):
    form = TelForm(initial={'tel_number': '+81123456789'})
    return render(request, 'home.html', {'form': form})
