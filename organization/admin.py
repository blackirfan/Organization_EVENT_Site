from django.contrib import admin
from .models import Organization,Special_event
# in here need to register the app name
admin.site.register(Organization)
admin.site.register(Special_event)
