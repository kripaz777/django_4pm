from django.db import models
# python manage.py makemigrations
# python manage.py migrate
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=50)
    subject = models.TextField()
    message = models.TextField()

