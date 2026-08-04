from django.db import models
from django.contrib.auth.models import AbstractUser


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
