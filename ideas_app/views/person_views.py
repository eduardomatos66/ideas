from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import PersonForm
from ..models import Person
from ..serializers import PersonSerializer
from rest_framework import permissions
from rest_framework import viewsets


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Person to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]


def form_person(request, person_id=0):
    if request.method == 'GET':
        if person_id == 0:
            form = PersonForm()
        else:
            instance = Person.objects.get(pk=person_id)
            form = PersonForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if person_id == 0:
            form = PersonForm(request.POST)
        else:
            person = Person.objects.get(pk=person_id)
            form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_person(request, person_id):
    return render(request, 'index.html')


def list_person(request):
    person_list = Person.objects.all()
    template = loader.get_template('index.html')
    context = {
        'items_list': person_list,
    }
    return HttpResponse(template.render(context, request))
