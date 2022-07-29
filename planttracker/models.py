import datetime as dt

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


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


class Possession(models.Model):
    """
    plants owned by a particular sprouter, along with metadata about plant
    the sprouter can indiciate the frequency in which they'd like to take action
    on the plant, such as number of days between watering/fertilizing/repotting
    """
    sprouter = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    nickname = models.CharField(
        max_length=100,
        help_text="enter nickname that can be used to refer to this plant"
    )
    days_water = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=True,
        null=True,
        help_text="frequency in which plant should be watered",
        verbose_name="days between watering"
    )
    days_fertilize = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=True,
        null=True,
        help_text="frequency in which plant should be fertilized",
        verbose_name="days between fertilization"
    )
    days_repot = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=True,
        null=True,
        help_text="frequency in which plant should be repotted",
        verbose_name="days between repotting"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("model-detail-view", args=[str(self.id)])
    
    def __str__(self):
        return self.nickname


class Activity(models.Model):
    """tracks activity conducted on plant posession"""

    class ActionType(models.TextChoices):
        ACQUIRED = "AQ", _("Acquired")
        WATERED = "WT", _("Watered")
        FERTILIZED = "FZ", _("Fertilized")
        REPOTTED = "RP", _("Repotted")

    posession = models.ForeignKey(Possession, on_delete=models.CASCADE)
    action = models.CharField(
        max_length=20,
        choices=ActionType.choices,
        blank=False
    )
    activity_date = models.DateField(
        default=now,
        null=False,
        blank=False,
        help_text="date in which activity took place."
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
