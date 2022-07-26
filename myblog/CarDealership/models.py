from django.db import models
from django.forms import IntegerField


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.DateField()
    hp = models.IntegerField()
    color = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.CharField(max_length=20)


class Client(models.Model):
    mail = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)


class Receipt(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    # cascade (какскадное удаление) означает удаление связанное с этой записью (удаляем запись = удаляем машину и клиента)
    # do_nothing тут задействован, чтобы ничего не удалилось
