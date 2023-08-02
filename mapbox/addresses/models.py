import geocoder

from django.db import models

access_token = 'pk.eyJ1IjoiZ3Vra2EtIiwiYSI6ImNsa3RtMjNzMDAxd3UzZnIwZmlvN3d1cmgifQ.lEK2iW44G1IfkzcUQhIufA' # mapbox access token


class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)


    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latlng # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
