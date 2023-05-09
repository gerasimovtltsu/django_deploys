from django.test import TestCase
from mysite.models import Person, StudentGroup

class PersonTest(TestCase):
    def setUp(self):
        self.group = StudentGroup.objects.create(group='Группа1', entry_year=2023, department='Институт ...')
        self.person = Person.objects.create(name='Студент1', age=18, info=self.group)
    
    def test_get_items(self):
        person2 = Person.objects.get(name='Студент1', age=18)