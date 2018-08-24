from devices.models import Device, Property
from rest_framework import serializers
from django.db.models.fields import BinaryField
from rest_framework.fields import ModelField
from devices.utils import serialize_content_data
from rest_framework.decorators import action

class ContentField(serializers.Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return serialize_content_data(self.context['request'].data['type'], data)


class PropertySerializer(serializers.ModelSerializer):
    content = ContentField(source='content_data')

    class Meta:
        model = Property
        fields = ('id', 'device', 'name', 'type', 'content')


class DeviceSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)
    lookup_field = 'id'
    
    class Meta:
        model = Device
        fields = ('id', 'name', 'properties')
