from django.db import models


# Create your models here.

class Avmform(models.Model):
    name = models.CharField(max_length=120)
    fathername = models.CharField(max_length=120)
    batch = models.IntegerField()
    passout = models.IntegerField()
    mobile = models.CharField(max_length=10)
    presentaddress = models.TextField()
    permanentaddress = models.TextField()
    occupation = models.CharField(max_length=250)
    workaddress = models.TextField()
    qualification = models.CharField(max_length=50, default=None)
    DOB = models.DateField()
    whatsapp = models.CharField(max_length=12, null=True, blank=True, default=None)
    interest = models.TextField(null=True, blank=True, default=None)
    achievement = models.TextField(default=None, null=True, blank=True)
    organization = models.TextField(null=True, blank=True, default=None)
    improvement = models.TextField(null=True, blank=True, default=None)
    suggestion = models.TextField(null=True, blank=True, default=None)
    DOW = models.DateField(null=True, blank=True)
    image_url = models.TextField()

    def __str__(self):
        return f"name: {self.name}, passout: {self.passout}"
