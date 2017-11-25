from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import generic
from django.utils import timezone
from datetime import datetime 
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import RunForm, ShiftForm
from .models import Shift, Run



def shift_list(request):
	s_query = Shift.objects.most_recent()
	return render(request, 'shifts/shift_list.html', {'s_query':s_query})

class DetailView(generic.DetailView):
    model = Shift
    template_name = 'shifts/detail.html'

def run_new(request):
	print 'Hello'
	if request.method == "POST":
		form = RunForm(request.POST)
		if form.is_valid():
			print 'Hi'
			run = form.save(commit=False)
			run.save()
			return HttpResponseRedirect('/')
	else:
		form = RunForm()
	return render(request, 'shifts/run_edit.html', {'form':form}) #edit

class GroupView(generic.DetailView):
    model = Shift
    template_name = 'shifts/group_new.html'



class ResultsView(generic.DetailView):
    model = Shift
    template_name = 'shifts/results.html'
    