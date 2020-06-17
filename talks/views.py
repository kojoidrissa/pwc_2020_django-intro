from django.shortcuts import get_object_or_404,render # NOQA
# https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/

from django.views.generic import TemplateView

from .models import Talk


class HomepageView(TemplateView):
    """
    Our default homepage for PWC Intro to Django Tutorial.
    It is NOT fancy.
    """

    template_name = "homepage.html"


def talk_list_view(request):
    """Create a list of all talks."""
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-all-objects
    talk_list = Talk.objects.all()
    context = {"talk_list": talk_list}
    return render(request, "talks/talk_list.html", context)


def talk_detail_view(request, id):
    """Return single talk."""
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-a-single-object-with-get
    # V2: https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#get-object-or-404 # NOQA
    single_talk = get_object_or_404(Talk, id=id)
    context = {"talk": single_talk, }
    return render(request, "talks/talk_detail.html", context)
