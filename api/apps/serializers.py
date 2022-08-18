from rest_framework import serializers
# Models
from apps.models import Room, Client, Booking, Payment
from apps.models.room_booking import RoomBooking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ['created_at', 'updated_at']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['created_at', 'updated_at']


class RoomBookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = RoomBooking
        exclude = ['id', 'booking', 'created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    rooms = RoomBookingSerializer(many=True)

    class Meta:
        model = Booking
        exclude = ['created_at', 'updated_at']


class RoomBookingField(serializers.DictField):
    room_id = serializers.IntegerField()
    rate = serializers.FloatField()


class BookingCreateSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
    date_from = serializers.DateField(format='%Y-%m-%d')
    date_to = serializers.DateField(format='%Y-%m-%d')
    number_of_adults = serializers.IntegerField()
    number_of_children = serializers.IntegerField()
    number_of_rooms = serializers.IntegerField()
    rooms = serializers.ListField(child=RoomBookingField(), min_length=1)


class PaymentCreateSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    payment_type = serializers.ChoiceField(choices=Payment.PAYMENT_TYPE_CHOICES)
    invoice_name = serializers.CharField()
    invoice_number = serializers.CharField()
