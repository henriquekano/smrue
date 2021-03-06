# -*- encoding:utf-8 -*-

from django.forms import ModelForm
from django import forms
from goal.models import Goal
from equipment.models import Equipment
from consumption.models import Consumption

from django.contrib.auth.models import Group, User

class GoalForm(ModelForm):
  name = forms.CharField(required=True, label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
  value_in_percent = forms.DecimalField(required=True, label='Gasto Relativo (%)', widget=forms.TextInput(attrs={'class': 'form-control percent-mask'}))
  yearmonth_start = forms.DateField(label='Data de Começo', widget=forms.HiddenInput())
  yearmonth_end = forms.DateField(label='Data de Fim', widget=forms.HiddenInput())
  equipment = forms.ModelChoiceField(required=True, label='Equipamento', queryset=Equipment.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

  class Meta:
      model = Goal
      fields = ['name', 'value_in_percent', 'equipment', 'yearmonth_start', 'yearmonth_end']
      exclude = ('created_at', 'updated_at', 'value_absolute')
