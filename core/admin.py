from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import HomepageSection, SiteSettings, User, WebsitePage


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(WebsitePage)
class WebsitePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'navigation_title', 'published', 'display_order')
    list_filter = ('published',)
    search_fields = ('title', 'slug', 'navigation_title', 'hero_title', 'content')
    ordering = ('display_order', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(HomepageSection)
class HomepageSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'published', 'display_order')
    list_filter = ('published', 'section_type')
    search_fields = ('title', 'subtitle', 'body', 'button_text')
    ordering = ('display_order', 'title')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'body', 'section_type', 'published', 'display_order'),
        }),
        ('Call to Action', {
            'fields': ('button_text', 'button_url'),
        }),
    )


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
