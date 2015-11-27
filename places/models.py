from django.contrib.gis.db import models
import json

class Place(models.Model):
    objects = models.GeoManager()
    osm_id = models.IntegerField()
    md5 = models.CharField(max_length=64, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)
    is_flooded = models.BooleanField(default=True)

    def get_geojson(self):
        return {
            'type': 'Feature',
            'geometry': json.loads(self.geom.geojson),
            'properties': json.loads(self.properties)
        }

    def __unicode__(self):
        return self.osm_id
