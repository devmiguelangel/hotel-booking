from django.db import models
# Models
from apps.models import Client


class Booking(models.Model):
    """ Booking model """

    BOOKING_STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagado'),
        ('cancelled', 'Cancelado'),
    ]

    id = models.BigAutoField(primary_key=True, editable=False)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='bookings')
    date_from = models.DateField()
    date_to = models.DateField()
    booking_status = models.CharField(max_length=30, choices=BOOKING_STATUS_CHOICES)
    number_of_adults = models.PositiveIntegerField()
    number_of_children = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'
        managed = True
        verbose_name = 'Booking'

    def __str__(self):
        return '{floor} - {room_number}'.format(floor=self.floor, room_number=self.room_number)
