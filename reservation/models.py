from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
     email = models.EmailField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Table(models.Model):
     seats = models.IntegerField()
     min_people = models.IntegerField()
     max_people = models.IntegerField()


class Reservation(models.Model):
     table = models.ForeignKey('Table', on_delete=models.CASCADE)
     party = models.CharField(max_length=255)
     spot = models.CharField(max_length=255)


