from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Furniture(models.Model):
    name = models.CharField(max_length=100)
    furnituretype = models.CharField(max_length=50,choices=(("chair","Chaise1"),("table","Table1")),default="chair")
    #Chair
    chairbacktype = models.CharField(max_length=50,choices=(("flat","Flat Back"),("rods","With Rods")),default="flat")
    thickness_backchair = models.IntegerField(default=5,validators=[MinValueValidator(5),MaxValueValidator(12)])
    nbrods = models.IntegerField(default=3,validators=[MinValueValidator(3),MaxValueValidator(10)])
    #table
    length = models.FloatField(default=0,validators=[MinValueValidator(100),MaxValueValidator(250)])
    width = models.FloatField(default=0,validators=[MinValueValidator(100),MaxValueValidator(2500)])
    height = models.FloatField(default=0,validators=[MinValueValidator(100),MaxValueValidator(2000)])
    # Ajoutez d'autres champs selon vos besoins

    def __str__(self):
        return self.name
