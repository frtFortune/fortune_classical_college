from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    TEACHER = 'teacher', 'Teacher'
    STUDENT = 'student', 'Student'


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.STUDENT,
    )


class WebsitePage(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title', help_text='The page title shown in the admin and on the public page when used.')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug', help_text='Unique URL-friendly identifier for this page.')
    navigation_title = models.CharField(max_length=100, blank=True, verbose_name='Navigation title', help_text='Short title used in navigation when needed.')
    hero_title = models.CharField(max_length=250, blank=True, verbose_name='Hero title', help_text='Main headline for the page hero section.')
    hero_subtitle = models.CharField(max_length=400, blank=True, verbose_name='Hero subtitle', help_text='Supporting text shown beneath the hero title.')
    content = models.TextField(blank=True, verbose_name='Page content', help_text='Main editable body content for this page.')
    seo_title = models.CharField(max_length=200, blank=True, verbose_name='SEO title', help_text='Optional browser and search title override.')
    seo_description = models.CharField(max_length=300, blank=True, verbose_name='SEO description', help_text='Optional meta description for this page.')
    published = models.BooleanField(default=False, verbose_name='Published', help_text='Only published pages should appear publicly.')
    display_order = models.PositiveIntegerField(default=0, verbose_name='Display order', help_text='Controls ordering for page lists and navigation.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = 'Website Page'
        verbose_name_plural = 'Website Pages'

    def __str__(self):
        return self.title or self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class HomepageSection(models.Model):
    class SectionType(models.TextChoices):
        WELCOME = 'WELCOME', 'Welcome'
        HIGHLIGHTS = 'HIGHLIGHTS', 'Highlights'
        WHY_CHOOSE_US = 'WHY_CHOOSE_US', 'Why Choose Us'
        PROGRAMMES = 'PROGRAMMES', 'Programmes'
        FACILITIES = 'FACILITIES', 'Facilities'
        CTA = 'CTA', 'Call to Action'
        FAQ_PREVIEW = 'FAQ_PREVIEW', 'FAQ Preview'
        CONTACT_PREVIEW = 'CONTACT_PREVIEW', 'Contact Preview'

    title = models.CharField(max_length=200, verbose_name='Title', help_text='Heading for the section.')
    subtitle = models.CharField(max_length=300, blank=True, verbose_name='Subtitle', help_text='Optional supporting line for this section.')
    body = models.TextField(blank=True, verbose_name='Body', help_text='Main textual content for the section.')
    button_text = models.CharField(max_length=100, blank=True, verbose_name='Button text', help_text='Optional call-to-action button label.')
    button_url = models.CharField(max_length=300, blank=True, verbose_name='Button URL', help_text='Optional destination for the call-to-action button.')
    section_type = models.CharField(max_length=30, choices=SectionType.choices, verbose_name='Section type', help_text='Type of section this content belongs to on the homepage.')
    display_order = models.PositiveIntegerField(default=0, verbose_name='Display order', help_text='Controls the order of this section on the homepage.')
    published = models.BooleanField(default=False, verbose_name='Published', help_text='Only published sections appear on the public homepage.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = 'Homepage Section'
        verbose_name_plural = 'Homepage Sections'

    def __str__(self):
        return self.title or self.get_section_type_display()


class SiteSettings(models.Model):
    school_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='School name',
        help_text='The public name shown across the website.',
    )
    short_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Short name',
        help_text='A shorter name used in compact navigation or headings.',
    )
    motto = models.CharField(
        max_length=250,
        blank=True,
        verbose_name='Motto',
        help_text='A short slogan or guiding statement for the school.',
    )
    primary_phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Primary phone',
        help_text='Primary public contact phone number.',
    )
    secondary_phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Secondary phone',
        help_text='Secondary public contact phone number.',
    )
    email = models.EmailField(
        blank=True,
        verbose_name='Email address',
        help_text='Primary public email address.',
    )
    address = models.TextField(
        blank=True,
        verbose_name='Address',
        help_text='Postal or physical address for the school.',
    )
    office_hours = models.CharField(
        max_length=250,
        blank=True,
        verbose_name='Office hours',
        help_text='General office hours shown on the public site.',
    )
    hero_title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name='Hero title',
        help_text='Main headline displayed on the home page hero section.',
    )
    hero_subtitle = models.CharField(
        max_length=400,
        blank=True,
        verbose_name='Hero subtitle',
        help_text='Supporting text displayed under the hero title.',
    )
    footer_text = models.TextField(
        blank=True,
        verbose_name='Footer text',
        help_text='Text shown in the global website footer.',
    )
    facebook_url = models.URLField(blank=True, verbose_name='Facebook URL', help_text='Public Facebook page URL.')
    instagram_url = models.URLField(blank=True, verbose_name='Instagram URL', help_text='Public Instagram profile URL.')
    x_url = models.URLField(blank=True, verbose_name='X URL', help_text='Public X/Twitter profile URL.')
    youtube_url = models.URLField(blank=True, verbose_name='YouTube URL', help_text='Public YouTube channel URL.')
    linkedin_url = models.URLField(blank=True, verbose_name='LinkedIn URL', help_text='Public LinkedIn profile URL.')
    default_meta_description = models.CharField(
        max_length=300,
        blank=True,
        verbose_name='Default meta description',
        help_text='Fallback meta description for public pages.',
    )
    logo = models.FileField(
        upload_to='site/logo/',
        blank=True,
        null=True,
        verbose_name='Logo',
        help_text='Optional logo file for the public website.',
    )
    favicon = models.FileField(
        upload_to='site/favicon/',
        blank=True,
        null=True,
        verbose_name='Favicon',
        help_text='Optional favicon file for the public website.',
    )
    hero_image = models.FileField(
        upload_to='site/hero/',
        blank=True,
        null=True,
        verbose_name='Hero image',
        help_text='Optional hero image file for the website homepage.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.school_name or self.short_name or 'Site Settings'

    def save(self, *args, **kwargs):
        if self.pk is not None:
            super().save(*args, **kwargs)
            return
        if SiteSettings.objects.exists():
            raise ValueError('Only one SiteSettings record can be created.')
        super().save(*args, **kwargs)
