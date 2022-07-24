from distutils.command.upload import upload
from turtle import title
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models
from django.utils import timezone
from email.mime import image
from tabnanny import verbose
from django.urls import reverse
# from requests import post


# Create your models here.


class About(models.Model):
    first_name = models.CharField('Ism', max_length=20)
    last_name = models.CharField('Familiya', max_length=20)
    date_birth = models.IntegerField('Tugilgan kun')
    motto = models.TextField('Shior')
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        'Rasm', null=True, blank=True, upload_to='files/uploads')

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.first_name


class Card(models.Model):
    image = models.ImageField(
        'Rasm', null=True, blank=True, upload_to='files/uploads')
    text = models.CharField('Izoh', max_length=4)
    title = models.TextField('Sarlavha', max_length=200)
    description = models.TextField('Izoh', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    create_at = models.DateTimeField(
        'Tarqatingan sanasi', null=True, blank=True)
    views = models.IntegerField(
        'Korinishlar soni', default=0, null=True, blank=True)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('about', kwargs={'slug': self.slug})


class Rasm(models.Model):
    image = models.ImageField(
        'Rasm', null=True, blank=True, upload_to='files/uploads')

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"

    def __str__(self):
        return 'Image'


class Karta(models.Model):
    image = models.ImageField(
        'Rasm', null=True, blank=True, upload_to='files/uploads')
    title = models.TextField('Sarlavha', max_length=10)

    class Meta:
        verbose_name = "Karta"
        verbose_name_plural = "Kartalar"

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField(
        'Rasm', null=True, blank=True, upload_to='files/uploads')
    title = models.TextField('Sarlavha', max_length=20)
    data = models.DateTimeField('Vaqt')

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"

    def __str__(self):
        return self.title
