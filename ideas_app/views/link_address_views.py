from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import LinkAddressForm
from ..models import LinkAddress


def form_link_address(request, link_address_id=0):
    if request.method == 'GET':
        if link_address_id == 0:
            form = LinkAddressForm()
        else:
            instance = LinkAddress.objects.get(pk=link_address_id)
            form = LinkAddressForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if link_address_id == 0:
            form = LinkAddressForm(request.POST)
        else:
            link_address = LinkAddress.objects.get(pk=link_address_id)
            form = LinkAddressForm(request.POST, instance=link_address)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_link_address(request, link_address_id):
    return render(request, 'index.html')


def list_link_address(request):
    link_address_list = LinkAddress.objects
    template = loader.get_template('index.html')
    context = {
        'items_list': link_address_list,
    }
    return HttpResponse(template.render(context, request))
