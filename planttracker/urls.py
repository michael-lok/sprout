from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("plants/", views.PlantView.as_view(), name="plants"),
    path("possessions/", views.PossessionView.as_view(), name="possessions")
]


# detail urls
urlpatterns += [
    path("plants/<int:pk>", views.PlantDetailView.as_view(), name="plant-detail"),
    path("possessions/<int:pk>", views.PossessionDetailView.as_view(), name="possession-detail")
]
