from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import Account, UserProfile


# Register your models here.
class AccountAdmin(UserAdmin):
    """
    Creating list of fields which are readonly, links and
    display, also password hashing is implemented
    """
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    """Register User Profile"""
    def thumbnail(self, object):
        """Create a thumbnail image"""
        return format_html('<img src="{}" width="30" style="border-radius:50%">'.format(object.profile_img.url))
    thumbnail.short_description = "Procfile Picture"
    list_display = ('user', 'town_or_city', 'country')


admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
