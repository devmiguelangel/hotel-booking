from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Views
from apps.views import RoomViewSet, ClientViewSet, BookingViewSet

# Routers
router = DefaultRouter(trailing_slash=False)
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
