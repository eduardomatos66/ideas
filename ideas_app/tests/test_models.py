import datetime

from django.test import TestCase

from ..models import Person, Professor, ResidenceStudent, Institute, Researcher, LinkAddress, Idea, ResearchInfo, \
    MonographInfo


class TestPerson(TestCase):

    def setUp(self):
        self.person = Person.objects.create(name='eduardo josé de vasconcelos matos', email='ejvm@cin.ufpe.br')

    def test_person_title_name(self):
        self.assertEquals(self.person.name, 'Eduardo José De Vasconcelos Matos')

    def test_wrong_person_title_name(self):
        self.assertNotEquals(self.person.name, 'eduardo josé de vasconcelos matos')

    def test_person_email(self):
        self.assertEquals(self.person.email, 'ejvm@cin.ufpe.br')

    def test_wrong_person_email(self):
        self.assertNotEqual(self.person.email, 'ejv@cin.ufpe.br')


class TestInstitute(TestCase):
    def setUp(self):
        self.institute = Institute.objects.create(short_name='CIn/UFPE',
                                                  long_name='Center of Informatics on Federal University of Pernambuco')

    def test_institute_short_name(self):
        self.assertEquals(self.institute.short_name, 'CIN/UFPE')

    def test_institute_long_name(self):
        self.assertEquals(self.institute.long_name, 'Center of Informatics on Federal University of Pernambuco')

    def test_wrong_institute_long_name(self):
        self.assertNotEquals(self.institute.long_name, 'Centre of Informatics on Federal of Pernambuco')


class TestProfessor(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='eduardo matos', email='ejvm@cin.ufpe.br')
        self.institute = Institute.objects.create(short_name='CIn/UFPE',
                                                  long_name='Center of Informatics on University')
        self.professor = Professor.objects.create(person=self.person, institute=self.institute)

    def test_professor_name(self):
        self.assertEquals(self.professor.person.name, 'Eduardo Matos')

    def test_professor_email(self):
        self.assertEquals(self.professor.person.email, 'ejvm@cin.ufpe.br')

    def test_professor_institute(self):
        self.assertEquals(self.professor.institute.short_name, 'CIN/UFPE')


class TestResidenceStudent(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='eduardo matos', email='ejvm@cin.ufpe.br')
        self.institute = Institute.objects.create(short_name='CIn/UFPE',
                                                  long_name='Center of Informatics on University')
        self.residence_student = ResidenceStudent.objects.create(
            person=self.person,
            residence_class='Class22',
            core_id='eduardomatos',
            institute=self.institute,
            team='DevTools')

    def test_residence_student_person(self):
        local_person = Person.objects.get(name='Eduardo Matos')
        self.assertEquals(self.residence_student.person, local_person)

    def test_residence_student_class(self):
        self.assertEquals(self.residence_student.residence_class, 'Class22')

    def test_residence_student_core_id(self):
        self.assertEquals(self.residence_student.core_id, 'eduardomatos')

    def test_residence_student_institute(self):
        local_institute = Institute.objects.get(short_name='CIN/UFPE')
        self.assertEquals(self.residence_student.institute, local_institute)

    def test_residence_student_team(self):
        self.assertEquals(self.residence_student.team, 'DevTools')


class TestResearcher(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='eduardo matos', email='ejvm@cin.ufpe.br')
        self.institute = Institute.objects.create(short_name='CIn/UFPE',
                                                  long_name='Center of Informatics on University')
        self.researcher = Researcher.objects.create(
            person=self.person,
            core_id='eduardomatos',
            institute=self.institute,
            team_org='Research team'
        )

    def test_researcher_person(self):
        local_person = Person.objects.get(name='Eduardo Matos')
        self.assertEquals(self.researcher.person, local_person)

    def test_researcher_core_id(self):
        self.assertEquals(self.researcher.core_id, 'eduardomatos')

    def test_researcher_institute(self):
        local_institute = Institute.objects.get(short_name='CIN/UFPE')
        self.assertEquals(self.researcher.institute, local_institute)

    def test_researcher_team_org(self):
        self.assertEquals(self.researcher.team_org, 'Research team')


class TestLinkAddress(TestCase):
    def setUp(self):
        self.link_address = LinkAddress.objects.create(url='https://www.google.com/', description='Google\'s Searcher')

    def test_link_address_url(self):
        self.assertEquals(self.link_address.url, 'https://www.google.com/')

    def test_link_address_description(self):
        self.assertEquals(self.link_address.description, 'Google\'s Searcher')


class TestIdea(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name='eduardo matos', email='ejvm@cin.ufpe.br')
        self.person2 = Person.objects.create(name='raphael farias', email='rfc@cin.ufpe.br')
        self.link_address1 = LinkAddress.objects.create(url='https://www.google.com/', description='Google\'s Searcher')
        self.link_address2 = LinkAddress.objects.create(url='https://www.amazon.com/', description='Amazon\'s Searcher')
        self.idea = Idea.objects.create(
            key='IDEA_0001',
            title='Title for idea 0001',
            description='Long description for idea 0001 - Lorem Ipsum is simply dummy text of the printing and '
                        'typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since '
                        'the 1500s, when an unknown printer took a galley of type and scrambled it to make a type '
                        'specimen book. It has survived not only five centuries, but also the leap into electronic '
                        'typesetting, remaining essentially unchanged. It was popularised in the 1960s with the '
                        'release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                        'publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
            keywords='key_1, key2, keyword3',
            progress='NOT STARTED',
            suggested_by=self.person1.name,
            impacted_areas='Test areas impacted by Idea',
            priority='3',
            register_date=datetime.date.today(),
            comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                     'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                     'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                     'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat '
                     'non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

        self.idea.suggested_po.add(self.person1)
        self.idea.suggested_po.add(self.person2)
        self.idea.related_links.add(self.link_address1)
        self.idea.related_links.add(self.link_address2)

    def test_idea_key(self):
        self.assertEquals(self.idea.key, 'IDEA_0001')

    def test_idea_title(self):
        self.assertEquals(self.idea.title, 'Title for idea 0001')

    def test_idea_description(self):
        self.assertEquals(self.idea.description,
                          'Long description for idea 0001 - Lorem Ipsum is simply dummy text of the printing and '
                          'typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since '
                          'the 1500s, when an unknown printer took a galley of type and scrambled it to make a type '
                          'specimen book. It has survived not only five centuries, but also the leap into electronic '
                          'typesetting, remaining essentially unchanged. It was popularised in the 1960s with the '
                          'release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                          'publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

    def test_idea_keywords(self):
        self.assertEquals(self.idea.keywords, 'key_1, key2, keyword3')

    def test_idea_progress(self):
        self.assertEquals(self.idea.progress, 'NOT STARTED')

    def test_idea_suggested_by(self):
        local_person = Person.objects.get(name='Eduardo Matos')
        self.assertEquals(self.idea.suggested_by, local_person.name)

    def test_idea_impacted_areas(self):
        self.assertEquals(self.idea.impacted_areas, 'Test areas impacted by Idea')

    def test_idea_suggested_po(self):
        self.assertTrue(self.person2 in self.idea.suggested_po.all())

    def test_idea_priority(self):
        self.assertEquals(self.idea.priority, '3')

    def test_idea_related_links(self):
        link_address1 = LinkAddress.objects.get(url='https://www.google.com/')
        link_address2 = LinkAddress.objects.get(url='https://www.amazon.com/')
        self.assertTrue(link_address1 in self.idea.related_links.all())
        self.assertTrue(link_address2 in self.idea.related_links.all())

    def test_wrong_idea_related_links(self):
        link_address1 = LinkAddress.objects.create(url='https://www.google.com.br/',
                                                   description='Link not added to idea')
        self.assertFalse(link_address1 in self.idea.related_links.all())

    def test_idea_register_date(self):
        self.assertEquals(self.idea.register_date, datetime.date.today())

    def test_idea_comments(self):
        self.assertEquals(self.idea.comments, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do '
                                              'eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad '
                                              'minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip '
                                              'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                                              'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur '
                                              'sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt'
                                              ' mollit anim id est laborum.')


class TestResearchInfo(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name='eduardo matos', email='ejvm@cin.ufpe.br')
        self.link_address = LinkAddress.objects.create(url='https://www.google.com/', description='Google\'s Searcher')
        self.idea = Idea.objects.create(
            key='IDEA_0001',
            title='Title for idea 0001',
            description='Long description for idea 0001 - Lorem Ipsum is simply dummy text of the printing and '
                        'typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since '
                        'the 1500s, when an unknown printer took a galley of type and scrambled it to make a type '
                        'specimen book. It has survived not only five centuries, but also the leap into electronic '
                        'typesetting, remaining essentially unchanged. It was popularised in the 1960s with the '
                        'release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                        'publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
            keywords='key_1, key2, keyword3',
            progress='NOT STARTED',
            suggested_by=self.person1.name,
            impacted_areas='Test areas impacted by Idea',
            priority='3',
            register_date=datetime.date.today(),
            comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                     'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                     'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                     'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat '
                     'non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

        self.idea.suggested_po.add(self.person1)
        self.idea.related_links.add(self.link_address)
        self.institute = Institute.objects.create(short_name='CIn/UFPE',
                                             long_name='Center of Informatics on University')
        self.researcher = Researcher.objects.create(
            person=self.person1,
            core_id='eduardomatos',
            institute=self.institute,
            team_org='Research team'
        )
        self.person2 = Person.objects.create(name='Flávia Barros', email='fab@cin.ufpe.br')
        self.institute1 = Institute.objects.create(short_name='INDT', long_name='Institute Nokia of Technology')
        self.professor = Professor.objects.create(person=self.person2, institute=self.institute1)

        self.research_info = ResearchInfo.objects.create(
            research_key='RESEARCH_INFO_0001',
            idea_key=self.idea,
            title='Title for the research..',
            progress='NOT_STARTED',
            researcher=self.researcher,
            research_type='Master Degree',
            professor=self.professor,
            impacted_project_test_area='',
            start_date=datetime.date.today() - datetime.timedelta(days=20),
            due_date=datetime.date.today() + datetime.timedelta(days=10),
            org='Team or organization',
            group='G3',
            comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                     'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                     'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                     'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat '
                     'non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.Lorem ipsum dolor '
                     'sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore '
                     'magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut '
                     'aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse '
                     'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, '
                     'sunt in culpa qui officia deserunt mollit anim id est laborum.'
        )
        self.research_info.po.add(self.person2)

    def test_research_info_research_key(self):
        self.assertEquals(self.research_info.research_key, 'RESEARCH_INFO_0001')

    def test_research_info_idea_key(self):
        self.assertEquals(self.research_info.idea_key.key, 'IDEA_0001')

    def test_research_info_title(self):
        self.assertEquals(self.research_info.title, 'Title for the research..')

    def test_research_info_progress(self):
        self.assertEquals(self.research_info.progress, 'NOT_STARTED')

    def test_research_info_researcher(self):
        self.assertEquals(self.research_info.researcher.core_id, 'eduardomatos')

    def test_research_info_research_type(self):
        self.assertEquals(self.research_info.research_type, 'Master Degree')

    def test_research_info_professor(self):
        self.assertEquals(self.research_info.professor.person.email, 'fab@cin.ufpe.br')

    def test_research_info_po(self):
        self.assertEquals(self.research_info.po.all()[0].email, self.person2.email)

    def test_research_info_impacted_project_test_area(self):
        self.assertEquals(self.research_info.impacted_project_test_area, '')

    def test_research_info_start_date(self):
        self.assertEquals(self.research_info.start_date, datetime.date.today() - datetime.timedelta(days=20))

    def test_research_info_due_date(self):
        self.assertEquals(self.research_info.due_date, datetime.date.today() + datetime.timedelta(days=10))

    def test_research_info_org(self):
        self.assertEquals(self.research_info.org, 'Team or organization')

    def test_research_info_group(self):
        self.assertEquals(self.research_info.group, 'G3')

    def test_research_info_comments(self):
        self.assertEquals(self.research_info.comments, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                                                       'sed do eiusmod tempor incididunt ut labore et dolore magna '
                                                       'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                                                       'ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis '
                                                       'aute irure dolor in reprehenderit in voluptate velit esse '
                                                       'cillum dolore eu fugiat nulla pariatur. Excepteur sint '
                                                       'occaecat cupidatat non proident, sunt in culpa qui officia '
                                                       'deserunt mollit anim id est laborum.Lorem ipsum dolor sit '
                                                       'amet, consectetur adipiscing elit, sed do eiusmod tempor '
                                                       'incididunt ut labore et dolore magna aliqua. Ut enim ad minim '
                                                       'veniam, quis nostrud exercitation ullamco laboris nisi ut '
                                                       'aliquip ex ea commodo consequat. Duis aute irure dolor in '
                                                       'reprehenderit in voluptate velit esse cillum dolore eu fugiat '
                                                       'nulla pariatur. Excepteur sint occaecat cupidatat non '
                                                       'proident, sunt in culpa qui officia deserunt mollit anim id '
                                                       'est laborum.')


class TestMonographInfo(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='eduardo matos', email='ejvm@cin.ufpe.br')
        self.institute = Institute.objects.create(short_name='CIn/UFPE',
                                                  long_name='Center of Informatics on University')
        self.residence_student = ResidenceStudent.objects.create(
            person=self.person,
            residence_class='Class22',
            core_id='eduardomatos',
            institute=self.institute,
            team='DevTools')

        self.person1 = Person.objects.create(name='raphael farias', email='rfc@cin.ufpe.br')
        self.link_address = LinkAddress.objects.create(url='https://www.google.com.br/',
                                                       description='BR Google\'s Searcher')
        self.idea = Idea.objects.create(
            key='IDEA_0001',
            title='Title for idea 0001',
            description='Long description for idea 0001 - Lorem Ipsum is simply dummy text of the printing and '
                        'typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since '
                        'the 1500s, when an unknown printer took a galley of type and scrambled it to make a type '
                        'specimen book. It has survived not only five centuries, but also the leap into electronic '
                        'typesetting, remaining essentially unchanged. It was popularised in the 1960s with the '
                        'release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '
                        'publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
            keywords='key_1, key2, keyword3',
            progress='NOT STARTED',
            suggested_by=self.person1.name,
            impacted_areas='Test areas impacted by Idea',
            priority='3',
            register_date=datetime.date.today(),
            comments='Lorem ipsum dolor sit amet')

        self.idea.suggested_po.add(self.person1)
        self.idea.related_links.add(self.link_address)

        self.person2 = Person.objects.create(name='Flávia Barros', email='fab@cin.ufpe.br')
        self.institute1 = Institute.objects.create(short_name='INDT', long_name='Institute Nokia of Technology')
        self.professor = Professor.objects.create(person=self.person2, institute=self.institute1)

        self.link_address1 = LinkAddress.objects.create(url='https://www.google.com/', description='Google\'s Searcher')
        self.link_address2 = LinkAddress.objects.create(url='https://www.amazon.com/', description='Amazon\'s Searcher')

        self.monograph_info = MonographInfo.objects.create(
            monograph_key='MONOGRAPH_INFO-0001',
            idea_key=self.idea,
            title='This is a title for the Monograph work',
            residence_class='T30',
            comments='Lorem ipsum dolor sit amet')

        self.monograph_info.student.add(self.residence_student)
        self.monograph_info.po.add(self.person1)
        self.monograph_info.professor.add(self.professor)
        self.monograph_info.related_links.add(self.link_address1)
        self.monograph_info.related_links.add(self.link_address2)

    def test_monograph_info_monograph_key(self):
        self.assertEquals(self.monograph_info.monograph_key, 'MONOGRAPH_INFO-0001')

    def test_monograph_info_idea_key(self):
        self.assertEquals(self.monograph_info.idea_key.key, 'IDEA_0001')

    def test_monograph_info_title(self):
        self.assertEquals(self.monograph_info.title, 'This is a title for the Monograph work')

    def test_monograph_info_residence_class(self):
        self.assertEquals(self.monograph_info.residence_class, 'T30')

    def test_monograph_info_student(self):
        self.assertEquals(self.monograph_info.student.all()[0].core_id, 'eduardomatos')

    def test_monograph_info_professor(self):
        self.assertEquals(self.monograph_info.professor.all()[0], self.professor)

    def test_monograph_info_po(self):
        self.assertEquals(self.monograph_info.po.all()[0].email, 'rfc@cin.ufpe.br')

    def test_monograph_info_comments(self):
        self.assertEquals(self.monograph_info.comments, 'Lorem ipsum dolor sit amet')

    def test_monograph_info_related_links(self):
        self.assertEquals(len(self.monograph_info.related_links.all()), 2)


class TestDevToolsProject(TestCase):
    def setUp(self):
        # TODO create tests
        pass
