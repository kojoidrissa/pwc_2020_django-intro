from django.contrib import admin

from .models import Talk

# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#modeladmin-objects


class TalkAdmin(admin.ModelAdmin):
    """The ModelAdmin class is the representation of a model in the admin."""

    list_display = ["talk_title"]
    search_fields = [
        "personal_name",
        "family_name",
        "talk_title",
        "contact_email",
        "twitter_handle",
    ]


admin.site.register(Talk, TalkAdmin)
