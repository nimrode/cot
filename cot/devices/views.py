from rest_framework import viewsets
from rest_framework.response import Response
from devices.models import Device, Property
from devices.serializers import DeviceSerializer, PropertySerializer
from rest_framework.decorators import action, api_view


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(methods=['get'], detail=True)
    def properties(self, request, pk):
        device = Device.objects.get(pk=pk)
        serializer = DeviceSerializer(instance=device)
        return Response(serializer.data['properties'])
    
    @api_view(['get'])
    def single_property(request, pk, property):
        device = Device.objects.get(pk=pk)
        desired_property = device.properties.filter(name=property).first()
        serializer = PropertySerializer(instance=desired_property)
        return Response(serializer.data)

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

