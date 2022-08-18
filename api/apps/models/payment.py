from django.db import models
# Models
from apps.models import Booking


class Payment(models.Model):
    """ Payment model """

    PAYMENT_TYPE_CHOICES = [
        ('credit_card', 'Tarjeta de Crédito'),
        ('debit_card', 'Tarjeta de Débito'),
        ('cash', 'Efectivo'),
        ('mobile', 'Pago por móvil'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Pagado'),
        ('not_paid', 'No Pagado'),
    ]

    id = models.BigAutoField(primary_key=True, editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT, related_name='payments')
    payment_date = models.DateTimeField()
    amount = models.FloatField()
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payments'
        managed = True
        verbose_name = 'Payment'

    def __str__(self):
        return '{room} - {payment_date}'.format(room=self.room, payment_date=self.payment_date)
