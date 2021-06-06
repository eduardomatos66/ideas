from django.forms import ModelForm
from .models import *


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class ResidenceStudentForm(ModelForm):
    class Meta:
        model = ResidenceStudent
        fields = '__all__'


class ResearcherForm(ModelForm):
    class Meta:
        model = Researcher
        fields = '__all__'


class LinkAddressForm(ModelForm):
    class Meta:
        model = LinkAddress
        fields = '__all__'


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'


class ResearchInfoForm(ModelForm):
    class Meta:
        model = ResearchInfo
        fields = '__all__'


class MonographInfoForm(ModelForm):
    class Meta:
        model = MonographInfo
        fields = '__all__'


class DevToolsProjectForm(ModelForm):
    class Meta:
        model = DevToolsProject
        fields = '__all__'
