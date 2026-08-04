from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def academics(request):
    return render(request, 'academics.html')


def admissions(request):
    return render(request, 'admissions.html')


def news(request):
    return render(request, 'news.html')


def faq(request):
    return render(request, 'faq.html')


def contact(request):
    return render(request, 'contact.html')


def login_view(request):
    return render(request, 'login.html')
