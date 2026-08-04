from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('admissions/', views.admissions, name='admissions'),
    path('news/', views.news, name='news'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
]
