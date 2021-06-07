from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import ResearchInfoForm
from ..models import ResearchInfo
from ..serializers import ResearchInfoSerializer
from rest_framework import permissions
from rest_framework import viewsets


class ResearchInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ResearchInfo to be viewed or edited.
    """
    queryset = ResearchInfo.objects.all()
    serializer_class = ResearchInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


def form_research_info(request, research_info_id=0):
    if request.method == 'GET':
        if research_info_id == 0:
            form = ResearchInfoForm()
        else:
            instance = ResearchInfo.objects.get(pk=research_info_id)
            form = ResearchInfoForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if research_info_id == 0:
            form = ResearchInfoForm(request.POST)
        else:
            research_info = ResearchInfo.objects.get(pk=research_info_id)
            form = ResearchInfoForm(request.POST, instance=research_info)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_research_info(request, research_info_id):
    return render(request, 'index.html')


def list_research_info(request):
    research_info_list = ResearchInfo.objects.all()
    template = loader.get_template('index.html')
    context = {
        'items_list': research_info_list,
    }
    return HttpResponse(template.render(context, request))
