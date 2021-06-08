import datetime

from django.test import TestCase

from ..models import Person, Professor, ResidenceStudent, Institute, Researcher, LinkAddress, Idea


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
        # TODO create tests
        pass


class TestMonographInfo(TestCase):
    def setUp(self):
        # TODO create tests
        pass


class TestDevToolsProject(TestCase):
    def setUp(self):
        # TODO create tests
        pass
