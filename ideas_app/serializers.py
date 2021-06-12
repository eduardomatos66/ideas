from .models import Person, Professor, ResidenceStudent, Researcher, LinkAddress, Idea, ResearchInfo, MonographInfo, \
    DevToolsProject, Institute
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'email']


class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields = ['person', 'institute']


class ResidenceStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResidenceStudent
        fields = ['person', 'residence_class', 'core_id', 'institute', 'team']


class ResearcherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Researcher
        fields = ['person', 'core_id', 'institute', 'team_org']


class LinkAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkAddress
        fields = ['url', 'description']


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = ['key', 'title', 'description', 'keywords', 'progress', 'suggested_by', 'impacted_areas',
                  'suggested_po', 'priority', 'related_links', 'register_date', 'comments']


class ResearchInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResearchInfo
        fields = ['research_key', 'idea_key', 'title', 'progress', 'researcher', 'research_type', 'professor', 'po',
                  'impacted_project_test_area', 'start_date', 'due_date', 'org', 'group', 'comments']


class MonographInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonographInfo
        fields = ['monograph_key', 'idea_key', 'title', 'residence_class', 'student', 'professor', 'po', 'comments',
                  'related_links']


class DevToolsProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DevToolsProject
        fields = ['idea_key', 'monograph_key', 'research_key', 'tool_key', 'tool_name', 'status', 'current_version',
                  'dependencies', 'start_date', 'due_date', 'devs', 'po', 'related_links', 'comments']


class InstituteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institute
        fields = ['short_name', 'long_name']
