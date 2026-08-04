from django.shortcuts import render

from .models import WebsitePage


def home(request):
    return render(request, 'home.html')


def _get_page(request, slug):
    page = WebsitePage.objects.filter(slug=slug, published=True).first()
    return {
        'page': page,
        'hero_title': page.hero_title if page else None,
        'hero_subtitle': page.hero_subtitle if page else None,
        'content': page.content if page else '',
        'page_title': page.title if page else None,
    }


def about(request):
    return render(request, 'about.html', _get_page(request, 'about'))


def academics(request):
    return render(request, 'academics.html')


def admissions(request):
    return render(request, 'admissions.html', _get_page(request, 'admissions'))


def news(request):
    return render(request, 'news.html')


def faq(request):
    return render(request, 'faq.html', _get_page(request, 'faq'))


def contact(request):
    return render(request, 'contact.html', _get_page(request, 'contact'))


def login_view(request):
    return render(request, 'login.html')
