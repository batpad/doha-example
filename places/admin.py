from django.contrib.gis import admin
from models import *
from leaflet.admin import LeafletGeoAdmin


class PlaceAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Place, PlaceAdmin)

