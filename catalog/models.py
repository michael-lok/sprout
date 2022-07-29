from django.contrib.auth.models import User
from django.db import models

# Create your models here.
sprouter = models.ForeignKey(
    User, on_delete=models.SET_NULL,
    null=True,
    blank=True
)

