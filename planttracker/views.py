from django.db.models import Count
from django.shortcuts import render
from django.views import generic

from .models import (
    Plant,
    Possession,
    Activity
)


def index(request):
    """view function for home page of site."""
    num_plants = Plant.objects.all().count()
    num_sprouters = Possession.objects.all().annotate(
        Count("sprouter", distinct=True)
    )
    num_possessions = Possession.objects.all().count()
    num_activity = Activity.objects.all().count()

    return render(
        request,
        "index.html",
        context={
            "num_plants": num_plants,
            "num_sprouters": num_sprouters,
            "num_possessions": num_possessions,
            "num_activity": num_activity
        }
    )


class PlantView(generic.ListView):
    model = Plant
    paginate_by = 10
