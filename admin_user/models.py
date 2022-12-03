from django.db import models

# Create your models here.
class Course(models.Model):

    title = models.CharField(max_length=256)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    second_date_from = models.DateTimeField()
    second_date_to = models.DateTimeField()
    description = models.TextField()
    address = models.TextField()
    kecamatan = models.CharField(max_length=256)
    kabupaten = models.CharField(max_length=256)
    provinsi = models.CharField(max_length=256)
    contacts = models.TextField()
    image = models.BinaryField()