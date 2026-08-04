from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import SiteSettings, User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identity', {
            'fields': ('school_name', 'short_name', 'motto'),
        }),
        ('Contact', {
            'fields': ('primary_phone', 'secondary_phone', 'email', 'address', 'office_hours'),
        }),
        ('Homepage', {
            'fields': ('hero_title', 'hero_subtitle'),
        }),
        ('Footer and Social', {
            'fields': ('footer_text', 'facebook_url', 'instagram_url', 'x_url', 'youtube_url', 'linkedin_url'),
        }),
        ('SEO', {
            'fields': ('default_meta_description',),
        }),
        ('Media', {
            'fields': ('logo', 'favicon', 'hero_image'),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
