from django.forms import ModelForm
from models import Job, Client, Grade, Competency
from django import forms

class JobForm(ModelForm):
	class Meta:
		model= Job
		exclude = ('code_j',)

class ClientForm(ModelForm):
	class Meta:
		model= Client
		exclude = ('code_u',)

class GradeForm(ModelForm):
	class Meta:
		model= Grade
		exclude = ('code_g',)

class CompetencyForm(ModelForm):
	class Meta:
		model= Competency
		exclude = ('code_c',)
