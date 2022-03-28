from django.core.mail import EmailMessage
from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True)
    show = models.BooleanField(default=False)
    slug = models.TextField(max_length=20,unique=True)
    description = models.TextField()


    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

class Clients(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()





    def __str__(self):
        if self.name and self.phone_number:
            return f'{self.name} | {self.phone_number}'
        elif self.name:
            return f'{self.name}'
        elif self.phone_number:
            return f'{self.phone_number}'
        else:
            return ''