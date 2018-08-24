from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import DeviceViewSet, PropertyViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'devices', DeviceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path(r'devices/<int:pk>/properties/<str:property>', DeviceViewSet.single_property, name="device-single-property")
]
