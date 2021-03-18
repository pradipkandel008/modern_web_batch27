from django.db import models
from django.core import validators
from django.core.validators import *

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image_url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Person(models.Model):
    firstname = models.CharField(max_length=200, null=True,
                                 validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=200, null=True,
                                validators=[validators.MinLengthValidator(2)])
    email = models.EmailField(unique=True, null=True, validators=[validate_email])
    phone = models.CharField(max_length=20, null=True,
                             validators=[validators.MinLengthValidator(9)])


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    batch = models.CharField(max_length=20)
    image_url = models.CharField(max_length=2000)
    category = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)


class FileUpload(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='static/uploads')









