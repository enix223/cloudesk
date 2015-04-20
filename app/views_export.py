#encoding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
from django.forms import ModelForm
from django.forms.util import ValidationError
from time import time
import re

# User define module
from app.models import Connection
from app.models import DB_TYPES, EXPORT_FILE_TYPE
from helper.db_export import MSSQLExporter


class ConnectionForm(ModelForm):

    class Meta:
        model = Connection


class ExportForm(forms.Form):
    sql = forms.CharField(label='SQL', required=True)
    export_types = forms.ChoiceField(label='Export type', choices=EXPORT_FILE_TYPE)
    filename = forms.CharField(label='File name')

    def __init__(self, user, *args, **kwargs):
        super(ExportForm, self).__init__(*args, **kwargs)
        self.fields['connection'] = forms.ChoiceField(label='DB Type',
                                                      choices=[(c.id, c.name) for c in Connection.objects.filter(owner=user)])

    def clean_filename(self):
        filename = self.cleaned_data['filename']
        if not re.search(r'^[\w\.\_\- ]+$', filename):
            raise ValidationError('File name not correct. Should be [a-zA-Z . - _]')
        return filename


@login_required
def config(request):
    connections = Connection.objects.filter(owner=request.user)
    return render(request, 'config.html', {'dbtypes': DB_TYPES, 'connections': connections, })


@login_required
def config_add(request):
    if request.method == 'GET':
        return redirect('db-config')
    else:
        form = ConnectionForm(request.POST)
        if form.is_valid():
            form.save()  # save a connection
            connections = Connection.objects.filter(owner=request.user)
            return render(request, 'config.html', {'dbtypes': DB_TYPES, 'connections': connections,
                                                   'msg': 'Connection created successfully.', })
        else:
            connections = Connection.objects.all()
            return render(request, 'config.html', {'dbtypes': DB_TYPES, 'connections': connections,
                                                   'msg': 'Parameters not correct.', })


@login_required
def config_edit(request, conn_id):
    if request.method == 'GET':
        form = get_object_or_404(Connection, pk=conn_id)
        connections = Connection.objects.all()
        return render(request, 'config.html', {'form': form, 'dbtypes': DB_TYPES, 'connections': connections, })
    else:
        con = get_object_or_404(Connection, pk=conn_id)
        form = ConnectionForm(request.POST or None, instance=con)
        if form.is_valid():

            form.save()  # save a connection
            connections = Connection.objects.filter(owner=request.user)
            return render(request, 'config.html', {'dbtypes': DB_TYPES, 'connections': connections,
                                                   'msg': 'Connection created successfully.', })
        else:
            connections = Connection.objects.filter(owner=request.user)
            return render(request, 'config.html', {'form': form, 'dbtypes': DB_TYPES, 'connections': connections,
                                                   'msg': 'Parameters not correct.', })


@login_required
def config_delete(request, conn_id):
    conn = get_object_or_404(Connection, pk=conn_id)
    conn.delete()
    return redirect('db-config')


@login_required
def exporter(request):
    if request.method == 'GET':
        form = ExportForm(request.user)
        connections = Connection.objects.filter(owner=request.user)
        return render(request, 'exporter.html', {'form': form, 'connections': connections,
                      'export_types': EXPORT_FILE_TYPE, })
    else:
        form = ExportForm(request.user, request.POST)
        if form.is_valid():
            # get the parameters
            choice = int(form.cleaned_data['export_types'])
            export_ext = re.search(r'(?<=\.)\w+(?=\))', dict(form.fields['export_types'].choices)[choice]).group()
            filename = '{filename}.{ext}'.format(filename=form.cleaned_data['filename'], ext=export_ext)

            # Create an exporter instance
            conn = Connection.objects.get(pk=form.cleaned_data['connection'])
            inst = MSSQLExporter(conn)

            # save result to http response
            response = HttpResponse(content_type='text/' + export_ext)
            response['Content-Disposition'] = 'attachment; filename=' + filename
            inst.export_to_xlsx(form.cleaned_data['sql'], response)
            return response
        else:
            connections = Connection.objects.filter(owner=request.user)
            return render(request, 'exporter.html', {'form': form, 'connections': connections,
                          'export_types': EXPORT_FILE_TYPE, })


@login_required
def parser(request):
    '''if request.method == 'GET':
        return render(request, 'parser.html', {'form': form})
    else:
        if form.is_valid():
            # <TO-DO> Do something
            con = get_object_or_404(Connection, pk=form.connection)
            pass
    '''
    pass


@login_required
def list_connect(request):
    conns = ConnectionForm.object.all
    return render(request, 'conn-list.html', {'conns': conns})

