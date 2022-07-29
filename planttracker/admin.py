from django.contrib import admin

from .models import (
    Plant,
    Possession
)


admin.site.register(Plant)
admin.site.register(Possession)
