from django import forms

from project.models import StudentGroup, Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"