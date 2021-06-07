from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import DevToolsProjectForm
from ..models import DevToolsProject
from ..serializers import DevToolsProjectSerializer
from rest_framework import permissions
from rest_framework import viewsets


class DevToolsProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DevToolsProject to be viewed or edited.
    """
    queryset = DevToolsProject.objects.all()
    serializer_class = DevToolsProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


def form_dev_tools_project(request, dev_tools_project_id=0):
    if request.method == 'GET':
        if dev_tools_project_id == 0:
            form = DevToolsProjectForm()
        else:
            instance = DevToolsProject.objects.get(pk=dev_tools_project_id)
            form = DevToolsProjectForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if dev_tools_project_id == 0:
            form = DevToolsProjectForm(request.POST)
        else:
            dev_tools_project = DevToolsProject.objects.get(pk=dev_tools_project_id)
            form = DevToolsProjectForm(request.POST, instance=dev_tools_project)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_dev_tools_project(request, dev_tools_project_id):
    return render(request, 'index.html')


def list_dev_tools_project(request):
    dev_tools_project_list = DevToolsProject.objects.all()
    template = loader.get_template('index.html')
    context = {
        'items_list': dev_tools_project_list,
    }
    return HttpResponse(template.render(context, request))
