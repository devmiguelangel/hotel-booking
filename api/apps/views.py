from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
# Models
from apps.models import Room, Client, Booking, RoomBooking, Payment
# Serializers
from apps.serializers import (RoomSerializer, ClientSerializer, BookingSerializer,
                              BookingCreateSerializer, PaymentCreateSerializer)
# Utils
import datetime


class RoomViewSet(ViewSet):
    """ Room view set """

    def list(self, request):
        """
        It takes a request, gets all the rooms from the database, serializes them, and returns them as a response

        :param request: The request object
        :return: A list of all the rooms in the database.
        """
        rooms = Room.objects.filter(room_status='available').order_by('floor', 'room_number')

        room_data = RoomSerializer(rooms, many=True).data

        return Response(room_data)

    def create(self, request):
        """
        It creates a room object and saves it to the database

        :param request: The request object
        :return: The room_data is being returned.
        """
        serializer = RoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        room = Room.objects.create(
            floor=data['floor'],
            room_type=data['room_type'],
            room_number=data['room_number'],
            description=data['description'],
            room_status=data['room_status'],
        )

        room_data = RoomSerializer(room).data

        return Response(room_data)


class ClientViewSet(ViewSet):
    """ Client api view set """

    def create(self, request):
        """
        It creates a new client object and saves it to the database

        :param request: The request object
        :return: The client object is being returned
        """
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        client = Client.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            dni=data['dni'],
            address=data['address'],
            country=data['country'],
            city=data['city'],
            phone_number=data['phone_number'],
            email=data['email'],
        )

        client_data = ClientSerializer(client).data

        return Response(client_data)

    def update(self, request, pk=None):
        """
        It takes the data from the request, validates it, and then updates the client with the new data

        :param request: The request object
        :param pk: The primary key of the client to be updated
        :return: The client data is being returned.
        """
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        try:
            client = Client.objects.get(pk=pk)

            client.first_name = data['first_name']
            client.last_name = data['last_name']
            client.address = data['address']
            client.country = data['country']
            client.city = data['city']
            client.phone_number = data['phone_number']
            client.email = data['email']

            client.save()

            client_data = ClientSerializer(client).data

            return Response(client_data)
        except Client.DoesNotExist as error:
            pass

        return Response(None, status=status.HTTP_404_NOT_FOUND)


class BookingViewSet(ViewSet):
    """ Booking view set """

    def create(self, request):
        """
        It creates a booking, creates a list of room bookings, and then returns the booking data

        :param request: The request object
        :return: The booking data is being returned.
        """
        serializer = BookingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        booking = Booking.objects.create(
            client_id=data['client_id'],
            date_from=data['date_from'],
            date_to=data['date_to'],
            booking_status='pending',
            number_of_adults=data['number_of_adults'],
            number_of_children=data['number_of_children'],
            number_of_rooms=data['number_of_rooms'],
        )

        rooms = []

        for room in data['rooms']:
            rooms.append(
                RoomBooking(
                    booking=booking,
                    room_id=room['room_id'],
                    rate=room['rate'],
                )
            )

        room_bookings = RoomBooking.objects.bulk_create(rooms)

        booking = Booking.objects.select_related('client').prefetch_related('rooms__room').get(pk=booking.pk)

        booking_data = BookingSerializer(booking).data

        return Response(booking_data)

    @action(detail=True, methods=['put'])
    def cancel(self, request, pk=None):
        """
        It gets a booking by its primary key, and if it exists, it sets its status to cancelled and returns the booking data

        :param request: The request object
        :param pk: The primary key of the booking to be deleted
        :return: The booking data is being returned
        """
        try:
            booking = Booking.objects.select_related('client').prefetch_related('rooms__room').get(pk=pk)

            booking.booking_status = 'deleted'
            booking.save()

            booking_data = BookingSerializer(booking).data

            return Response(booking_data)
        except Booking.DoesNotExist as error:
            pass

        return Response(None, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['put'])
    def pay(self, request, pk=None):
        """
        It creates a payment object and updates the booking status to paid

        :param request: The request object
        :param pk: The primary key of the object you want to retrieve
        :return: The booking data is being returned
        """
        serializer = PaymentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        try:
            booking = Booking.objects.select_related('client').prefetch_related('rooms__room').get(pk=pk)

            booking.payments.create(
                payment_date=datetime.datetime.now(),
                amount=data['amount'],
                payment_type=data['payment_type'],
                payment_status='paid',
                invoice_name=data['invoice_name'],
                invoice_number=data['invoice_number'],
            )

            for room_booking in booking.rooms.all():
                room_booking.room.room_status = 'reserved'
                room_booking.room.save()

            booking.booking_status = 'paid'
            booking.save()

            booking_data = BookingSerializer(booking).data

            return Response(booking_data)
        except Booking.DoesNotExist as error:
            pass

        return Response(None, status=status.HTTP_404_NOT_FOUND)
