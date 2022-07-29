from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


sprouter = models.ForeignKey(
    User, on_delete=models.SET_NULL,
    null=True,
    blank=True
)


class Plant(models.Model):
    """respresents plants available to be tracked."""
    scientific_name = models.CharField(
        max_length=200,
        help_text="scientific name given to plant"
    )
    common_name = models.CharField(
        max_length=100,
        help_text="name that plant is colloquially referred as"
    )
    custom_plant = models.BooleanField(
        default=False,
        help_text="plant added retroactively after initial USDA import"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("model-detail-view", args=[str(self.id)])

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"
