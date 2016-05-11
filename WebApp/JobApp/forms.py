from django.forms import ModelForm
from models import Job, User, Grade, Competency
from django import forms

class JobForm(ModelForm):
	class Meta:
		model= Job
		exclude = ('code_j',)

class UserForm(ModelForm):
	class Meta:
		model= User
		exclude = ('code_u',)

class GradeForm(ModelForm):
	class Meta:
		model= Grade
		exclude = ('code_g',)

class CompetencyForm(ModelForm):
	class Meta:
		model= Competency
		exclude = ('code_c',)
