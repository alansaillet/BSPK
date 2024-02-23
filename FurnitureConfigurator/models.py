from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Furnitures(models.Model):
    name = models.CharField(max_length=100)
    furnituretype = models.CharField(max_length=50,choices=(("chair","Chaise1"),("table","Table1")))
    #Chair
    chairbacktype = models.CharField(max_length=50,choices=(("flat","Flat Back"),("rods","With Rods")))
    thickness_backchair = models.IntegerField(validators=[MinValueValidator(5),MaxValueValidator(12)])
    nbrods = models.IntegerField(default=1,validators=[MinValueValidator(3),MaxValueValidator(10)])
    #table
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    # Ajoutez d'autres champs selon vos besoins

    def __str__(self):
        return self.name
