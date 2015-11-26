from models import Place
import json
from django.http import HttpResponse


def geojson(request):
    d = {
        'type': 'FeatureCollection',
        'features': [p.get_geojson() for p in Place.objects.all()]
    }
    return HttpResponse(json.dumps(d))
