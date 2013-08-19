# abstract.py
# Module for abstract mixin model classes
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime
from django.db.models.query import QuerySet

class SoftDeleteModelManager(models.Manager):
    def get_query_set(self):
        return SoftDeleteQuerySet(self.model)

class SoftDeleteQuerySet(QuerySet):
    def delete(self):
        self.update(deleted=True)

class SoftDeletable(models.Model):
    objects = SoftDeleteModelManager()
    deleted = models.BooleanField(default=False)
    class Meta:
        abstract = True

class Timestamps(models.Model):
    """Mixin that adds auto-updating timestamp fields."""
    created_at = models.DateTimeField(auto_now_add=True,
                                      default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True,
                                      default=datetime.datetime.now)

    class Meta:
        abstract = True

def validate_point(point):
    """Checking for valid location points"""

    if point.latitude < -90 or point.latitude > 90:
        raise ValidationError("latitude must be between "
                              "-90 and 90 degrees")
    if point.longitude < -180 or point.longitude > 180:
        raise ValidationError("longitude must be between "
                              "-180 and 180 degrees")

class Locatable(models.Model):
    """Mixin that gives a model location functionality."""
    latitude = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    def _get_point(self):
        if self.latitude and self.longitude:
            return Point(self.longitude, self.latitude)
        else:
            return Point(0, 0)

    def _set_point(self, point):
        self.latitude = point.y
        self.longitude = point.x
        self.save()

    point = property(_get_point, _set_point)

    class Meta:
        abstract = True
