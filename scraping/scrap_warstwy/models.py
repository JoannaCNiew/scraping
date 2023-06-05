from django.db import models

class Publisher(models.Model):
    id_publisher = models.IntegerField(primary_key=True)
    name_publisher = models.CharField(max_length=100)
    isbn_publisher = models.IntegerField(blank=True)
    email_publisher = models.EmailField(blank=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=15, null=True)
    edition = models.CharField(max_length=15, null=True)
    isbn = models.CharField(max_length=15, null=True)
    cover = models.CharField(max_length=15, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)


class Deposit(models.Model):
    id_deposit = models.IntegerField(primary_key=True)
    title_deposit = models.CharField(max_length=100)
    year_deposit = models.IntegerField()
    edition_deposit = models.IntegerField(blank=True)
    isbn_deposit = models.IntegerField(blank=True)
    form_deposit = models.CharField(max_length=15, blank=True)
    cover_deposit = models.CharField(max_length=15, blank=True)