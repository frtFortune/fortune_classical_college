from django.shortcuts import get_object_or_404, render

from .models import (
    HomepageSection,
    NewsItem,
    StaffProfile,
    WebsitePage,
)


def _get_homepage_sections():
    sections = HomepageSection.objects.filter(published=True).order_by('display_order', 'title')
    grouped = {
        'welcome': [],
        'highlights': [],
        'why_choose_us': [],
        'programmes': [],
        'facilities': [],
        'cta': [],
        'faq_preview': [],
        'contact_preview': [],
    }
    for section in sections:
        key = section.section_type.lower()
        if key in grouped:
            grouped[key].append(section)
    return grouped


def home(request):
    management_team = (
        StaffProfile.objects
        .filter(
            published=True,
            is_management=True,
        )
        .order_by(
            "display_order",
            "full_name",
        )
    )

    context = {
        "homepage_sections": _get_homepage_sections(),
        "management_team": management_team,
    }

    return render(
        request,
        "home.html",
        context,
    )


def _get_page_context(slug):
    page = WebsitePage.objects.filter(slug=slug, published=True).first()
    return {
        'page': page,
        'hero_title': page.hero_title if page else None,
        'hero_subtitle': page.hero_subtitle if page else None,
        'content': page.content if page else '',
        'page_title': page.title if page else None,
    }


def about(request):
    return render(request, 'about.html', _get_page_context('about'))


def academics(request):
    return render(request, 'academics.html', _get_page_context('academics'))


def admissions(request):
    return render(request, 'admissions.html', _get_page_context('admissions'))


def news_list(request):
    items = NewsItem.objects.filter(published=True).order_by('-publish_date', '-created_at', 'title')
    featured_items = items.filter(featured=True)[:3]
    context = {
        'items': items,
        'featured_items': featured_items,
    }
    return render(request, 'news/list.html', context)


def news_detail(request, slug):
    item = get_object_or_404(NewsItem, slug=slug, published=True)
    context = {'item': item}
    return render(request, 'news/detail.html', context)


def faq(request):
    return render(request, 'faq.html', _get_page_context('faq'))


def contact(request):
    return render(request, 'contact.html', _get_page_context('contact'))


def login_view(request):
    return render(request, 'login.html')


