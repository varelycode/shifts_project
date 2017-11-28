from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import generic
from django.utils import timezone
from datetime import datetime 
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import RunForm, ShiftForm
from .models import Shift, Run



def home(request):
	s_query = Shift.objects.most_recent()
	return render(request, 'shifts/home.html', {'s_query':s_query})
	
	
	
def shift_new(request, pk):

	if request.method == "POST":
		form = ShiftForm(request.POST)
		if form.is_valid():
			shift = form.save(commit=False)
			shift.save()
			return HttpRequest('/')
	else:
		form = ShiftForm()
	return render(request, 'shifts/shift_new.html', {'form':form}) #edit	
	

class DetailView(generic.DetailView):
    model = Shift
    template_name = 'shifts/detail.html'

def run_new(request, pk):

	shift = get_object_or_404(Shift, pk=pk)
	if request.method == "POST":
		form = RunForm(request.POST)
		if form.is_valid():
			run = form.save(commit=False)
			run.shift = shift # associate run with shift
			run.save()
			return redirect('detail', pk=shift.pk)
	else:
		form = RunForm()
	return render(request, 'shifts/run_edit.html', {'form':form}) #edit

class GroupView(generic.DetailView):
    model = Shift
    template_name = 'shifts/group_new.html'
