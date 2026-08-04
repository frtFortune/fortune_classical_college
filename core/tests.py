from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import HomepageSection, NewsItem, UserRole


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
