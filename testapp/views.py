from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TelForm, TelFormAttrs


def home(request):
    if request.POST:
        form = TelForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = TelForm()

    return render(request, 'home.html', {'form': form})


def attrs_test(request):
    form = TelFormAttrs()
    return render(request, 'home.html', {'form': form})
