#encoding: utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from django.forms import ModelForm

# User define module
from app.models import ConnectionModel

class ConnectionForm(ModelForm):
	class Meta:
		model = ConnectionModel
	
class ExportForm(forms.Form):
	sql = forms.TextField(label='SQL', required=True)

@login_required
def export(request):
	if(request.method == 'GET'):
		form = ExportForm()
		return render(request, 'export.html', {'form': form})
	else:
		form = ExportForm(request.POST)
		if(form.is_valid()):
			# <TO-DO> Do something
			pass
		
		
@login_required
def add_connect(request):
	if(request.method == 'GET'):
		form = ConnectionForm()
		return render(request, 'conn-edit.html', {'form': form})
	else:
		form = ConnectionForm(request.POST)
		if(form.is_valid()):
			form.save() # save a connection 
			return redirect('connection-list')
		else:			
			return render(request, 'conn-edit.html', {'form': form})

@login_required			
def edit_connect(request, conn_id):
	if(request.method == 'GET'):		
		conn = get_object_or_404(ConnectionModel, pk=conn_id)
		form = ConnectionForm(instance=con)
		return render(request, 'conn-edit.html', {'form': form})
	else:
		form = ConnectionForm(request.POST)
		if(form.is_valid()):
			form.save() # save a connection 
			return redirect('connection-list')
		else:			
			return render(request, 'conn-edit.html', {'form': form})

@login_required		
def list_connect(request):
	conns = ConnectionForm.object.all
	return render(request, 'conn-list.html', {'conns': conns})

	
	
	
	
	