from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TelForm


def home(request):
    if request.POST:
        form = TelForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = TelForm()

    return render(request, 'home.html', {'form': form})
