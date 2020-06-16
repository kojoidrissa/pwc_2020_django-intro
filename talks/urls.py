from django.urls import path # NOQA
# https://docs.djangoproject.com/en/3.0/topics/http/urls/

from . import views

# https://docs.djangoproject.com/en/3.0/ref/urls/#django.urls.path

# https://docs.djangoproject.com/en/3.0/topics/http/urls/#how-django-processes-a-request
# https://docs.djangoproject.com/en/3.0/topics/http/urls/#path-converters
urlpatterns = [
    path("", views.talk_list_view, name="talk-list"),
    path("<int:id>", views.talk_detail_view, name="talk-detail"),
]
