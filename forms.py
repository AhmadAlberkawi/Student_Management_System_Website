from django.forms import *
from studierendenverwaltung.models import *

class LehrveranstaltungForm(ModelForm):
    class Meta:
        model = Lehrveranstaltungen
        exclude = ()
        labels={'name': 'Name der Lehrveranstaltung'}


class StudentForm(ModelForm):
    class Meta:
        model = Studierende
        exclude = ()
