from models import Place
import json
from django.http import HttpResponse
from hashlib import md5

def geojson(request):
    d = {
        'type': 'FeatureCollection',
        'features': [p.get_geojson() for p in Place.objects.filter(is_flooded=True)]
    }
    return HttpResponse(json.dumps(d))


def save_geojson(request):
    data = json.loads(request.POST.get('data', None))
    if not data:
        return HttpResponse(json.dumps({'error': 'no data'}))
    osm_id = data['properties']['osm_id']
    geom_string = json.dumps(data['geometry'])
    feature_md5 = md5(geom_string + str(osm_id)).hexdigest()
    try:
        existing_place = Place.objects.get(md5=feature_md5)
        existing_place.is_flooded = data['properties']['is_flooded']
        existing_place.save()
        return HttpResponse(json.dumps(existing_place.get_geojson()))
    except:
        pass
    new_place = Place()
    new_place.osm_id = osm_id
    new_place.is_flooded = data['properties']['is_flooded']
    new_place.geom = json.dumps(data['geometry'])
    new_place.md5 = feature_md5
    new_place.properties = json.dumps(data['properties'])
    new_place.save()
    return HttpResponse(json.dumps(new_place.get_geojson()))
