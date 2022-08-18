from django.db import models


class Room(models.Model):
    """ Room model """

    ROOM_TYPE_CHOICES = [
        ('single', 'Simple'),
        ('double', 'Doble'),
        ('triple', 'Triple'),
        ('quad', 'Cuádruple'),
    ]

    ROOM_STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('reserved', 'Reservado'),
        ('occupied', 'Ocupado'),
    ]

    id = models.BigAutoField(primary_key=True, editable=False)
    floor = models.IntegerField()
    room_type = models.CharField(max_length=30, choices=ROOM_TYPE_CHOICES)
    room_number = models.IntegerField()
    description = models.TextField()
    room_status = models.CharField(max_length=30, choices=ROOM_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'rooms'
        managed = True
        verbose_name = 'Room'

    def __str__(self):
        return 'Floor {floor} - No. {room_number}'.format(floor=self.floor, room_number=self.room_number)
