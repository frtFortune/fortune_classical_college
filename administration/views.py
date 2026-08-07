from django.shortcuts import render


def dashboard(request):
    return render(request, "administration/dashboard.html")


def students(request):
    return render(request, "administration/students.html")


def classes(request):
    return render(request, "administration/classes.html")


def subjects(request):
    return render(request, "administration/subjects.html")


def teachers(request):
    return render(request, "administration/teachers.html")


def results(request):
    return render(request, "administration/results.html")


def external_results(request):
    return render(request, "administration/external_results.html")


def admissions(request):
    return render(request, "administration/admissions.html")


def settings(request):
    return render(request, "administration/settings.html")