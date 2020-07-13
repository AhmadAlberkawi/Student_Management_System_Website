from django.shortcuts import render
from forms import *
from studierendenverwaltung.models import *
from django.shortcuts import redirect
from django.contrib import messages

def student_list(request):
    students = Studierende.objects.all().order_by('nachname')
    return render(request, 'studierendenverwaltung/student_list.html',
                  {'page_title': 'Alle Studenten','students' : students,})

def lehrverantaltung_list(request):
    lerv =  Lehrveranstaltungen.objects.all()
    return render(request, 'studierendenverwaltung/lehrveranstaltung.html',
                  {'page_title': 'Studenten jenach Lehrveranstaltung','lerv' : lerv,})

def lehrveranstaltung_details(request, pk=None):
    if pk:
        lehrver = Lehrveranstaltungen.objects.get(pk=pk)
    else:
        lehrver = Lehrveranstaltungen()

    if request.method == 'POST':
        form = LehrveranstaltungForm(request.POST, instance=lehrver)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lehrveranstaltung gespeichert')
        return redirect('lehrverantaltung_list')
    else:
        form = LehrveranstaltungForm(instance=lehrver)

    return render(request, 'studierendenverwaltung/lehrveranstaltung_details.html',
                  {'page_title': 'Lehrveranstaltung hinzufügen/bearbeiten', 'form':form,})


def student_details(request, pk=None):
    if pk:
        student = Studierende.objects.get(pk=pk)
    else:
        student = Studierende()

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student gespeichert')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'studierendenverwaltung/student_details.html',
                  {'page_title': 'Student hinzufügen/bearbeiten', 'form':form,})


def lehrveranstaltung_delete(request, pk=None):
    if pk:
        lehrver = Lehrveranstaltungen.objects.get(pk=pk)
    else:
        lehrver = Lehrveranstaltungen()

    if request.method == 'POST':
        form = LehrveranstaltungForm(request.POST, instance=lehrver)
        if form.is_valid():
            lehrver.delete()
            return redirect('lehrverantaltung_list')
    else:
        form = LehrveranstaltungForm(instance=lehrver)

    return render(request, 'studierendenverwaltung/lehrveranstaltung_delete.html',
                  {'page_title': 'Lehrveranstaltung löschen', 'form':form,})

def student_delete(request, pk=None):
    if pk:
        student = Studierende.objects.get(pk=pk)
    else:
        student = Studierende()

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.delete()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'studierendenverwaltung/student_delete.html',
                  {'page_title': 'Student löschen', 'form':form,})

