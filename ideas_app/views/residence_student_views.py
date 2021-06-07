from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from ..forms import ResidenceStudentForm
from ..models import ResidenceStudent
from ..serializers import ResidenceStudentSerializer
from rest_framework import permissions
from rest_framework import viewsets


class ResidenceStudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ResidenceStudent to be viewed or edited.
    """
    queryset = ResidenceStudent.objects.all()
    serializer_class = ResidenceStudentSerializer
    permission_classes = [permissions.IsAuthenticated]


def form_residence_student(request, residence_student_id=0):
    if request.method == 'GET':
        if residence_student_id == 0:
            form = ResidenceStudentForm()
        else:
            instance = ResidenceStudent.objects.get(pk=residence_student_id)
            form = ResidenceStudentForm(instance=instance)
        return render(request, 'index.html', {'formset': form})
    else:
        if residence_student_id == 0:
            form = ResidenceStudentForm(request.POST)
        else:
            residence_student = ResidenceStudent.objects.get(pk=residence_student_id)
            form = ResidenceStudentForm(request.POST, instance=residence_student)
        if form.is_valid():
            form.save()
        return redirect('index.html')


def delete_residence_student(request, residence_student_id):
    return render(request, 'index.html')


def list_residence_student(request):
    residence_student_list = ResidenceStudent.objects.all()
    template = loader.get_template('index.html')
    context = {
        'items_list': residence_student_list,
    }
    return HttpResponse(template.render(context, request))
