from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import ResearcherForm
from ..models import Researcher


def form_researcher(request, researcher_id=0):
    if request.method == 'GET':
        if researcher_id == 0:
            form = ResearcherForm()
        else:
            instance = Researcher.objects.get(pk=researcher_id)
            form = ResearcherForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if researcher_id == 0:
            form = ResearcherForm(request.POST)
        else:
            researcher = Researcher.objects.get(pk=researcher_id)
            form = ResearcherForm(request.POST, instance=researcher)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_researcher(request, researcher_id):
    return render(request, 'index.html')


def list_researcher(request):
    researcher_list = Researcher.objects
    template = loader.get_template('index.html')
    context = {
        'items_list': researcher_list,
    }
    return HttpResponse(template.render(context, request))
