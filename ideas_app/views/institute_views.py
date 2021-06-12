from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import InstituteForm
from ..models import Institute
from ..serializers import InstituteSerializer
from rest_framework import permissions
from rest_framework import viewsets


class InstituteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Institute to be viewed or edited.
    """
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    permission_classes = [permissions.AllowAny]


def form_institute(request, institute_id=0):
    if request.method == 'GET':
        if institute_id == 0:
            form = InstituteForm()
        else:
            instance = Institute.objects.get(pk=institute_id)
            form = InstituteForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if institute_id == 0:
            form = InstituteForm(request.POST)
        else:
            institute = Institute.objects.get(pk=institute_id)
            form = InstituteForm(request.POST, instance=institute)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_institute(request, institute_id):
    return render(request, 'index.html')


def list_institute(request):
    institute_list = Institute.objects.all()
    template = loader.get_template('index.html')
    context = {
        'items_list': institute_list,
    }
    return HttpResponse(template.render(context, request))
