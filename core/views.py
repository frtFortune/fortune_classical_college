from django.shortcuts import render

from .models import HomepageSection, NewsItem, WebsitePage


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
        if section.section_type == HomepageSection.SectionType.WELCOME:
            grouped['welcome'].append(section)
        elif section.section_type == HomepageSection.SectionType.HIGHLIGHTS:
            grouped['highlights'].append(section)
        elif section.section_type == HomepageSection.SectionType.WHY_CHOOSE_US:
            grouped['why_choose_us'].append(section)
        elif section.section_type == HomepageSection.SectionType.PROGRAMMES:
            grouped['programmes'].append(section)
        elif section.section_type == HomepageSection.SectionType.FACILITIES:
            grouped['facilities'].append(section)
        elif section.section_type == HomepageSection.SectionType.CTA:
            grouped['cta'].append(section)
        elif section.section_type == HomepageSection.SectionType.FAQ_PREVIEW:
            grouped['faq_preview'].append(section)
        elif section.section_type == HomepageSection.SectionType.CONTACT_PREVIEW:
            grouped['contact_preview'].append(section)
    return grouped


def home(request):
    context = {'homepage_sections': _get_homepage_sections()}
    return render(request, 'home.html', context)


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


def news_list(request):
    items = NewsItem.objects.filter(published=True).order_by('-publish_date', '-created_at', 'title')
    featured_items = items.filter(featured=True)[:3]
    context = {
        'items': items,
        'featured_items': featured_items,
    }
    return render(request, 'news/list.html', context)


def news_detail(request, slug):
    item = NewsItem.objects.filter(slug=slug, published=True).first()
    context = {'item': item}
    return render(request, 'news/detail.html', context)


def faq(request):
    return render(request, 'faq.html', _get_page(request, 'faq'))


def contact(request):
    return render(request, 'contact.html', _get_page(request, 'contact'))


def login_view(request):
    return render(request, 'login.html')
