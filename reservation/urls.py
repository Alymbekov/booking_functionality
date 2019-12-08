from django.urls import path

from reservation.views import index, to_reserv, index_detail

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', index_detail, name='detail'),
    path('reserv/', to_reserv, name='reserv'),
]


