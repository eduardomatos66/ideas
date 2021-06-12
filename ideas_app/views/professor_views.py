from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import ProfessorForm
from ..models import Professor
from ..serializers import ProfessorSerializer
from rest_framework import permissions
from rest_framework import viewsets


class ProfessorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Professor to be viewed or edited.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.AllowAny]


def form_professor(request, professor_id=0):
    if request.method == 'GET':
        if professor_id == 0:
            form = ProfessorForm()
        else:
            instance = Professor.objects.get(pk=professor_id)
            form = ProfessorForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if professor_id == 0:
            form = ProfessorForm(request.POST)
        else:
            professor = Professor.objects.get(pk=professor_id)
            form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_professor(request, professor_id):
    return render(request, 'index.html')


def list_professor(request):
    professor_list = Professor.objects.all()
    template = loader.get_template('index.html')
    context = {
        'items_list': professor_list,
    }
    return HttpResponse(template.render(context, request))
