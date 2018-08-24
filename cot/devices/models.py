from django.db import models
from django.urls import reverse
from devices.utils import PropertyTypes, deserialize_content_data

import json

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('device', kwargs={'pk': self.pk})


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=9, choices=PropertyTypes.choices(), default=PropertyTypes.BINARY)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='properties')
    content_data = models.BinaryField()

    @property
    def content(self):
        return deserialize_content_data(self.type, self.content_data)
    