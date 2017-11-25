from django import forms

from .models import Shift, Run


class RunForm(forms.ModelForm):
	class Meta:
		model = Run
		fields = ('runs_text', 'runs_start', 'runs_end')
		
class ShiftForm(forms.ModelForm):
	class Meta:
		model = Shift
		fields = ('shifts_text', 'start_datetime', 'end_datetime')