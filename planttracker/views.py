from django.contrib import auth, messages
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import generic

from .forms import NewUserForm
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


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth.login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	return render(
        request=request,
        template_name="planttracker/register.html",
        context={"register_form":NewUserForm()}
    )


class PlantView(generic.ListView):
    model = Plant
    paginate_by = 10


class PlantDetailView(generic.DetailView):
    model = Plant


class PossessionView(generic.ListView):
    model = Possession
    pageinate_by = 10


class PossessionDetailView(generic.DetailView):
    model = Possession
