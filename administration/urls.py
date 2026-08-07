from django.urls import path
from . import views

app_name = "administration"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("students/", views.students, name="students"),
    path("classes/", views.classes, name="classes"),
    path("subjects/", views.subjects, name="subjects"),
    path("teachers/", views.teachers, name="teachers"),
    path("results/", views.results, name="results"),
    path(
        "external-results/",
        views.external_results,
        name="external_results",
    ),
    path("admissions/", views.admissions, name="admissions"),
    path("settings/", views.settings, name="settings"),
]