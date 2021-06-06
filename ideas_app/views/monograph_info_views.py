from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import MonographInfoForm
from ..models import MonographInfo


def form_monograph_info(request, monograph_info_id=0):
    if request.method == 'GET':
        if monograph_info_id == 0:
            form = MonographInfoForm()
        else:
            instance = MonographInfo.objects.get(pk=monograph_info_id)
            form = MonographInfoForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if monograph_info_id == 0:
            form = MonographInfoForm(request.POST)
        else:
            monograph_info = MonographInfo.objects.get(pk=monograph_info_id)
            form = MonographInfoForm(request.POST, instance=monograph_info)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_monograph_info(request, monograph_info_id):
    return render(request, 'index.html')


def list_monograph_info(request):
    monograph_info_list = MonographInfo.objects
    template = loader.get_template('index.html')
    context = {
        'items_list': monograph_info_list,
    }
    return HttpResponse(template.render(context, request))
