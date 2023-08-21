from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    year=models.IntegerField()
    img = models.ImageField(upload_to='gallery', null=True)
def __str__(self):
    return self.name
