from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Professor(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)
    institute = models.CharField(max_length=200)

    class Meta:
        ordering = ['person']

    def __str__(self):
        return self.person


class ResidenceStudent(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, null=False)
    residence_class = models.CharField(max_length=200)
    core_id = models.CharField(max_length=200)
    institution = models.CharField(max_length=200, null=False)
    team = models.CharField(max_length=200)

    class Meta:
        ordering = ['person']

    def __str__(self):
        return f'{self.person} ({self.core_id}) - T{self.residence_class}'


class Researcher(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, null=False)
    core_id = models.CharField(max_length=200)
    institution = models.CharField(max_length=200, null=False)
    team_org = models.CharField(max_length=200)

    class Meta:
        ordering = ['person', 'institution', 'team_org']

    def __str__(self):
        return f'{self.person} ({self.core_id}) - {self.team_org}'


class LinkAddress(models.Model):
    url = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ['url']

    def __str__(self):
        return self.url


class Idea(models.Model):
    class IdeaProgress(models.TextChoices):
        DEPLOYED = 'DEPLOYED'
        UNDER_DEVELOPMENT = 'UNDER DEVELOPMENT'
        UNDER_RESEARCH = 'UNDER RESEARCH'
        SCHOLARSHIP_WORK = 'SCHOLARSHIP WORK'
        NOT_STARTED = 'NOT STARTED'
    key = models.CharField(max_length=200, null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=False)
    keywords = models.CharField(max_length=200)
    progress = models.CharField(max_length=40, choices=IdeaProgress.choices, default=IdeaProgress.NOT_STARTED)
    suggested_by = models.CharField(max_length=200)
    impacted_areas = models.CharField(max_length=200)
    suggested_po = models.ManyToManyField('Person', related_name='ideas_po')
    priority = models.CharField(max_length=200)
    related_links = models.ManyToManyField('LinkAddress', related_name='ideas_link')
    register_date = models.DateField(default=timezone.now)
    comments = models.CharField(max_length=200)

    class Meta:
        ordering = ['key', 'progress', 'priority', 'register_date']

    def __str__(self):
        return f'{self.key}: {self.title}'


class ResearchInfo(models.Model):

    class ResearchProgress(models.TextChoices):
        IN_PROGRESS = 'IN PROGRESS'
        DISMISSED = 'DISMISSED'
        TOOL_SUBMIT = 'TOOL SUBMIT'
        DEPLOYED = 'DEPLOYED'
        ON_HOLD = 'ON HOLD'

    class ResearchType(models.TextChoices):
        DOCTOR_DEGREE = 'Doctor Degree'
        MASTER_DEGREE = 'Master Degree'
        SCIENTIFIC_INITIATION = 'Scientific Initiation'
        N_A = 'N/A'

    research_key = models.CharField(max_length=200, null=False)
    idea_key = models.ForeignKey(Idea, on_delete=models.DO_NOTHING, null=False)
    title = models.CharField(max_length=200, null=False)
    progress = models.CharField(max_length=40, choices=ResearchProgress.choices, default=ResearchProgress.IN_PROGRESS)
    researcher = models.CharField(max_length=40, choices=ResearchType.choices, default=ResearchType.N_A)
    research_type = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
    po = models.ManyToManyField('Person', related_name='research_infos_po')
    impacted_project_test_area = models.CharField(max_length=200)
    start_date = models.DateField(default=timezone.now)
    due_date = models.DateField(default=timezone.now)
    org = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)

    class Meta:
        ordering = ['research_key', 'idea_key', 'title', 'progress', 'professor', 'start_date', 'due_date', 'group']

    def __str__(self):
        return f'{self.research_key} ({self.idea_key}): {self.title}'


class MonographInfo(models.Model):
    monograph_key = models.CharField(max_length=200, null=False)
    idea_key = models.ForeignKey(Idea, on_delete=models.DO_NOTHING, null=False)
    title = models.CharField(max_length=200)
    residence_class = models.CharField(max_length=200, null=False)
    student = models.ManyToManyField('ResidenceStudent', related_name='monograph_infos_residence_student')
    professor = models.ManyToManyField('Professor', related_name='monograph_infos_professor')
    po = models.ManyToManyField('Person', related_name='monograph_infos_po')
    comments = models.CharField(max_length=200)
    related_links = models.ManyToManyField('LinkAddress', related_name='monograph_infos_link')

    class Meta:
        ordering = ['monograph_key', 'idea_key', 'title', 'residence_class']

    def __str__(self):
        return f'{self.monograph_key} ({self.idea_key}): {self.title}'


class DevToolsProject(models.Model):
    class ToolStatus(models.TextChoices):
        IN_PROGRESS = 'IN PROGRESS'
        DISMISSED = 'DISMISSED'
        TOOL_SUBMIT = 'TOOL SUBMIT'
        DEPLOYED = 'DEPLOYED'
        ON_HOLD = 'ON HOLD'
        PLANNED = 'PLANNED'
        EVALUATING = 'EVALUATING'
        STARTING = 'STARTING'

    idea_key = models.ForeignKey(Idea, on_delete=models.DO_NOTHING)
    monograph_key = models.ForeignKey(MonographInfo, on_delete=models.DO_NOTHING)
    research_key = models.ForeignKey(ResearchInfo, on_delete=models.DO_NOTHING)
    tool_key = models.CharField(max_length=200, null=False)
    tool_name = models.CharField(max_length=200, null=False)
    status = models.CharField(max_length=40, choices=ToolStatus.choices, default=ToolStatus.PLANNED)
    current_version = models.CharField(max_length=200)
    dependencies = models.CharField(max_length=200)
    start_date = models.DateField(default=timezone.now)
    due_date = models.DateField(default=timezone.now)
    devs = models.ManyToManyField('Person', related_name='dev_tools_projects_devs')
    po = models.ManyToManyField('Person', related_name='dev_tools_projects_po')
    related_links = models.ManyToManyField('LinkAddress', related_name='dev_tools_projects_link')
    comments = models.CharField(max_length=200)

    class Meta:
        ordering = ['idea_key', 'monograph_key', 'research_key', 'tool_key', 'tool_name', 'status', 'start_date',
                    'due_date']

    def __str__(self):
        return f'{self.tool_key} ({self.status}): {self.tool_name}'
