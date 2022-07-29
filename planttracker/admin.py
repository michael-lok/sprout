from django.contrib import admin

from .models import (
    Activity,
    Plant,
    Possession
)


admin.site.register(Plant)
admin.site.register(Possession)
admin.site.register(Activity)
