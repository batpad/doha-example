from django.contrib.gis.db import models
import json

class Place(models.Model):
    objects = models.GeoManager()
    title = models.CharField(max_length=255, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    def get_geojson(self):
        return {
            'type': 'Feature',
            'geometry': json.loads(self.geom.geojson),
            'properties': {
                'title': self.title
            }
        }

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return str(self.id)


# Create your models here.
