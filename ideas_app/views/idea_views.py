from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import IdeaForm
from ..models import Idea


def form_idea(request, idea_id=0):
    if request.method == 'GET':
        if idea_id == 0:
            form = IdeaForm()
        else:
            instance = Idea.objects.get(pk=idea_id)
            form = IdeaForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if idea_id == 0:
            form = IdeaForm(request.POST)
        else:
            idea = Idea.objects.get(pk=idea_id)
            form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_idea(request, idea_id):
    return render(request, 'index.html')


def list_idea(request):
    idea_list = Idea.objects.all()
    template = loader.get_template('index.html')
    context = {
        'items_list': idea_list,
    }
    return HttpResponse(template.render(context, request))
