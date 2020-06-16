from django.db import models

# https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

# https://docs.djangoproject.com/en/3.0/topics/db/models/


class Talk(models.Model):
    """The model for info about our talks."""

    personal_name = models.CharField(
        max_length=32, help_text="Commonly known as 'first name' in the US."
    )
    family_name = models.CharField(
        max_length=32, help_text="Commonly known as 'last name' in the US."
    )
    talk_title = models.CharField(max_length=64)
    contact_email = models.EmailField(max_length=200)
    twitter_handle = models.CharField(
        max_length=32,
        # This is how to make the field optional
        blank=True,
        null=True,
        help_text="This is optional. Leave the field blank, or enter your handle without the @ symbol."
    )
