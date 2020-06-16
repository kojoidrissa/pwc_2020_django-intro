from django.urls import path # NOQA
# https://docs.djangoproject.com/en/3.0/topics/http/urls/

from . import views

# https://docs.djangoproject.com/en/3.0/ref/urls/#django.urls.path
urlpatterns = [
    path("", views.list_view, name="talk-list"),
]
