from django.urls import path
from .views import HotelViewSet, RoomViewSet, BookingViewSet

urlpatterns = [
    path('', HotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='hotel_deatil'),
    path('', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room_deatil'),
    path('', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking_deatil'),

]
