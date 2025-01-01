from django.db import models

# Create your models here.
# Assuming you have a Django model like this:
class ContactEntry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

# Now, you can create and save an instance of the ContactEntry model:
from django.db import models

class SaveToDatabase(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


# photography/models.py
class Photo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    caption = models.TextField()

    def __str__(self):
        return self.name
