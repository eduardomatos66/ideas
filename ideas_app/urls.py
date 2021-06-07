"""ideas URL Configuration

The `urlpatterns` list routes URLs to _rlpatternsFor more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(''', _ aviews.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(''', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path(''blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from ideas_app.views import index, dev_tools_project_views, idea_views, link_address_views, monograph_info_views, \
    person_views, professor_views, research_info_views, researcher_views, residence_student_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'rs_dev_tools_project', dev_tools_project_views.DevToolsProjectViewSet)
router.register(r'rs_idea', idea_views.IdeaViewSet)
router.register(r'rs_link_address', link_address_views.LinkAddressViewSet)
router.register(r'rs_monograph_info', monograph_info_views.MonographInfoViewSet)
router.register(r'rs_person', person_views.PersonViewSet)
router.register(r'rs_professor', professor_views.ProfessorViewSet)
router.register(r'rs_research_info', research_info_views.ResearchInfoViewSet)
router.register(r'rs_researcher', researcher_views.ResearcherViewSet)
router.register(r'rs_residence_student', residence_student_views.ResidenceStudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', index.test, name='test'),
    path('person', person_views.form_person, name='form_person'),
    path('person/delete/<int:person_id>', person_views.delete_person, name='delete_person'),
    path('person/update/<int:person_id>', person_views.form_person, name='form_person'),
    path('person/list', person_views.list_person, name='list_person'),


    path('professor', professor_views.form_professor, name='form_professor'),
    path('professor/delete/<int:professor_id>', professor_views.delete_professor, name='delete_professor'),
    path('professor/update/<int:professor_id>', professor_views.form_professor, name='form_professor'),
    path('professor/list', professor_views.list_professor, name='list_professor'),


    path('residence_student', residence_student_views.form_residence_student, name='form_residence_student'),
    path('residence_student/delete/<int:residence_student_id>', residence_student_views.delete_residence_student,
         name='delete_residence_student'),
    path('residence_student/update/<int:residence_student_id>', residence_student_views.form_residence_student,
         name='form_residence_student'),
    path('residence_student/list', residence_student_views.list_residence_student, name='list_residence_student'),


    path('researcher', researcher_views.form_researcher, name='form_researcher'),
    path('researcher/delete/<int:researcher_id>', researcher_views.delete_researcher, name='delete_researcher'),
    path('researcher/update/<int:researcher_id>', researcher_views.form_researcher, name='form_researcher'),
    path('researcher/list', researcher_views.list_researcher, name='list_researcher'),


    path('link_address', link_address_views.form_link_address, name='form_link_address'),
    path('link_address/delete/<int:link_address_id>', link_address_views.delete_link_address,
         name='delete_link_address'),
    path('link_address/update/<int:link_address_id>', link_address_views.form_link_address,
         name='form_link_address'),
    path('link_address/list', link_address_views.list_link_address, name='list_link_address'),


    path('idea', idea_views.form_idea, name='form_idea'),
    path('idea/delete/<int:idea_id>', idea_views.delete_idea, name='delete_idea'),
    path('idea/update/<int:idea_id>', idea_views.form_idea, name='form_idea'),
    path('idea/list', idea_views.list_idea, name='list_idea'),


    path('research_info', research_info_views.form_research_info, name='form_research_info'),
    path('research_info/delete/<int:research_info_id>', research_info_views.delete_research_info,
         name='delete_research_info'),
    path('research_info/update/<int:research_info_id>', research_info_views.form_research_info,
         name='form_research_info'),
    path('research_info/list', research_info_views.list_research_info, name='list_research_info'),


    path('monograph_info', monograph_info_views.form_monograph_info, name='form_monograph_info'),
    path('monograph_info/delete/<int:monograph_info_id>', monograph_info_views.delete_monograph_info,
         name='delete_monograph_info'),
    path('monograph_info/update/<int:monograph_info_id>', monograph_info_views.form_monograph_info,
         name='form_monograph_info'),
    path('monograph_info/list', monograph_info_views.list_monograph_info, name='list_monograph_info'),


    path('dev_tools_project', dev_tools_project_views.form_dev_tools_project, name='form_dev_tools_project'),
    path('dev_tools_project/delete/<int:dev_tools_project_id>', dev_tools_project_views.delete_dev_tools_project,
         name='delete_dev_tools_project'),
    path('dev_tools_project/update/<int:dev_tools_project_id>', dev_tools_project_views.form_dev_tools_project,
         name='form_dev_tools_project'),
    path('dev_tools_project/list', dev_tools_project_views.list_dev_tools_project, name='list_dev_tools_project'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
