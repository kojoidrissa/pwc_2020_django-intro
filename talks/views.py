from django.shortcuts import render # NOQA
# https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/

from .models import Talk


def talk_list_view(request):
    """Create a list of all talks."""
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-all-objects
    talk_list = Talk.objects.all()
    context = {"talk_list": talk_list}
    return render(request, "talks/talk_list.html", context)


def talk_detail_view(request, id):
    """Return single talk."""
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-a-single-object-with-get
    single_talk = Talk.objects.get(id=id)
    context = {"talk": single_talk, }
    return render(request, "talks/talk_detail.html", context)
