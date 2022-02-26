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
