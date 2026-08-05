from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import HomepageSection, NewsItem, UserRole, WebsitePage


class UserRoleTests(SimpleTestCase):
    def test_user_role_choices_exclude_parent(self):
        choices = dict(UserRole.choices)

        self.assertEqual(set(choices), {'admin', 'teacher', 'student'})
        self.assertNotIn('parent', choices)


class HomePageTests(TestCase):
    def test_home_page_renders_published_homepage_sections(self):
        section = HomepageSection.objects.create(
            title='Featured Welcome',
            subtitle='A warm introduction',
            body='A welcoming message for families.',
            section_type=HomepageSection.SectionType.WELCOME,
            display_order=1,
            published=True,
        )

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Featured Welcome')
        self.assertContains(response, 'A welcoming message for families.')
        self.assertContains(response, f'aria-labelledby="section-heading-{section.pk}"')


class NewsItemTests(TestCase):
    def test_news_list_shows_published_items(self):
        NewsItem.objects.create(
            title='Campus Open Day',
            summary='An update for families.',
            content='A full announcement body.',
            published=True,
            featured=True,
        )

        response = self.client.get(reverse('news_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Campus Open Day')
        self.assertContains(response, 'An update for families.')

    def test_news_detail_renders_published_item(self):
        item = NewsItem.objects.create(
            title='Student Showcase',
            summary='A short preview.',
            content='The full story goes here.',
            published=True,
        )

        response = self.client.get(reverse('news_detail', kwargs={'slug': item.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Showcase')
        self.assertContains(response, 'The full story goes here.')

    def test_news_detail_returns_404_for_missing_or_unpublished_item(self):
        NewsItem.objects.create(
            title='Draft News',
            content='Draft text',
            published=False,
            slug='draft-news',
        )

        response_draft = self.client.get(reverse('news_detail', kwargs={'slug': 'draft-news'}))
        self.assertEqual(response_draft.status_code, 404)

        response_missing = self.client.get(reverse('news_detail', kwargs={'slug': 'non-existent'}))
        self.assertEqual(response_missing.status_code, 404)


class WebsitePageTests(TestCase):
    def test_academics_page_renders_with_placeholder_fallback(self):
        response = self.client.get(reverse('academics'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Academics Page')


