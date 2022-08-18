from django.db import models


class Client(models.Model):
    """ Client model """

    id = models.BigAutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    dni = models.CharField(max_length=14)
    address = models.TextField()
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clients'
        managed = True

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)
