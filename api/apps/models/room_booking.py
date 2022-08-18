from django.db import models
# Models
from apps.models import Booking, Room


class RoomBooking(models.Model):
    """ Room booking model """

    id = models.BigAutoField(primary_key=True, editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'room_bookings'
        managed = True
        verbose_name = 'Room Booking'

    def __str__(self):
        return '{booking} - {room}'.format(booking=self.booking, room=self.room)
