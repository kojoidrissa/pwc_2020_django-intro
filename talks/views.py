from django.shortcuts import render
# https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/

from .models import Talk


def list_view(request):
    """Create a list of all talks."""
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-all-objects
    talk_list = Talk.objects.all()
    context = {"talk_list": talk_list}
    return render(request, "talks/talk_list.html", context)
