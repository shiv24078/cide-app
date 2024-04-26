# cide_app/models.py

from django.db import models
import uuid

class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    dni = models.CharField(max_length=20)
    main_contact = models.CharField(max_length=255)
    contact_dni = models.CharField(max_length=20)
    email_contact = models.EmailField(max_length=100)
    phone_contact = models.CharField(max_length=20)
    enrollment_date = models.DateField()
    iban = models.CharField(max_length=34)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Course(models.Model):
    year = models.IntegerField()
    center = models.CharField(max_length=100, blank=True)
    course_name = models.CharField(max_length=100)
    tutor = models.CharField(max_length=100)

class Subject(models.Model):
    identifier = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Insurance(models.Model):
    annual_cost = models.DecimalField(max_digits=5, decimal_places=2)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
