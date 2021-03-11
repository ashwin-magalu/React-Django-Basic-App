from django.urls import path
from .views import RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateRoom

urlpatterns = [
    path('room/', RoomView.as_view()), # get request
    path('create-room/', CreateRoomView.as_view()), # post request
    path('get-room', GetRoom.as_view()), # get request
    path('join-room', JoinRoom.as_view()), # post request
    path('user-in-room', UserInRoom.as_view()), # get request
    path('leave-room', LeaveRoom.as_view()), # post request
    path('update-room', UpdateRoom.as_view()), # update/patch request
]