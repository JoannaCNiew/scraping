from django.db import models

class Publisher(models.Model):
    id_publisher = models.IntegerField(primary_key=True)
    name_publisher = models.CharField(max_length=100)
    isbn_publisher = models.IntegerField(blank=True)
    email_publisher = models.EmailField(blank=True)


class Book(models.Model):
    id_book = models.IntegerField(primary_key=True)
    title_book = models.CharField(max_length=100)
    year_book = models.IntegerField()
    edition_book = models.IntegerField(blank=True)
    isbn_book = models.IntegerField(blank=True)
    form_book = models.CharField(max_length=15, blank=True)
    cover_book = models.CharField(max_length=15, blank=True)


class Deposit(models.Model):
    id_deposit = models.IntegerField(primary_key=True)
    title_deposit = models.CharField(max_length=100)
    year_deposit = models.IntegerField()
    edition_deposit = models.IntegerField(blank=True)
    isbn_deposit = models.IntegerField(blank=True)
    form_deposit = models.CharField(max_length=15, blank=True)
    cover_deposit = models.CharField(max_length=15, blank=True)