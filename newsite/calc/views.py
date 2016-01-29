from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import AddForm
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			return HttpResponse(str(int(a)+int(b)))
	else:
		form = AddForm()
	return render(request, 'add.html', {'form': form})

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
	return HttpResponseRedirect(reverse('add2', args=(a, b)))

