from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery_images', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
