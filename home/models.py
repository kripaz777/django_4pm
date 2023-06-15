from django.db import models
# python manage.py makemigrations
# python manage.py migrate
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=50)
    subject = models.TextField()
    message = models.TextField()

class ContactInformation(models.Model):
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    time = models.CharField(max_length=50)

class Services(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=100)
    description = models.TextField()

class Feedback(models.Model):
    name = models.CharField(max_length= 300)
    post = models.CharField(max_length= 300)
    image = models.ImageField(upload_to='media')
    comment = models.TextField()
