from django.test import TestCase

from ..models import Person, Professor


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


class TestProfessor(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='eduardo matos', email='ejvm@cin.ufpe.br')
        self.professor = Professor.objects.create(person=self.person, institute='CIn/UFPE')

    def test_professor_name(self):
        self.assertEquals(self.professor.person.name, 'Eduardo Matos')

    def test_professor_email(self):
        self.assertEquals(self.professor.person.email, 'ejvm@cin.ufpe.br')

    def test_professor_institute(self):
        self.assertEquals(self.professor.institute, 'CIN/UFPE')

    def test_wrong_professor_institute(self):
        self.assertNotEquals(self.professor.institute, 'CIn/UFPE')


class TestResidenceStudent(TestCase):
    def setUp(self):
        pass


class TestResearcher(TestCase):
    def setUp(self):
        pass


class TestLinkAddress(TestCase):
    def setUp(self):
        pass


class TestIdea(TestCase):
    def setUp(self):
        pass


class TestResearchInfo(TestCase):
    def setUp(self):
        pass


class TestMonographInfo(TestCase):
    def setUp(self):
        pass


class TestDevToolsProject(TestCase):
    def setUp(self):
        pass
