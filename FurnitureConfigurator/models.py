from django.db import models

# Create your models here.
class TypeSelector(models.Model):
    type = models.CharField(max_length=100,choices=(("Chair","Chaise"),("Table","Table")))

class Table(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    style = models.CharField(max_length=100,choices=(("1","Type 1"),("2","Type 2")))
    # Ajoutez d'autres champs selon vos besoins

    def __str__(self):
        return self.name

class Chair(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    style = models.CharField(max_length=100,choices=(("1","Type 1"),("2","Type 2"),("3","Type 3")))
    # Ajoutez d'autres champs selon vos besoins

    def __str__(self):
        return self.name


class ChoiceAndSUbFields:
    def __init__(self,choiceField = None, subfields = []):
        self.choiceField = choiceField
        self.subfields = subfields
