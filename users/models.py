from django.db import models

# Create your models here.
class Shop(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name=models.CharField(max_length=266)
    price=models.FloatField()
    desc=models.TextField()
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.name}"
class Barber(models.Model):
    name=models.CharField(max_length=255)
    barber=models.ForeignKey(Category, on_delete=models.CASCADE ,null=True )
    def __str__(self):
        return f"{self.name}"
