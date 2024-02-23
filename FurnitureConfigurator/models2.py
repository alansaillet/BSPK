from django.db import models
import copy
from django.core.validators import MaxValueValidator, MinValueValidator

class FieldTree:
    def __init__(self,name, field):

        self.name = name
        self.field = field

        self.subfields = []
        self.parentChoice = None
        self.choice = None

    def setChoice(self,value):
        self.choice = value

    def add_subfield(self,parentChoice, subfield):
        subfield = copy.copy(subfield)
        subfield.parentChoice = parentChoice
        self.subfields.append(subfield)

    def print(self):
        print(self.parentChoice, self.name)
        for subfield in self.subfields:
            subfield.print()

root = FieldTree(name="type", field=models.CharField(max_length=100,choices=(("Chair","Chaise"),("Table","Table"))))

chairbacktype = FieldTree(name="chairbacktype", field=models.CharField(choices=(("flat","flat"),("rods","rods"))))
thickness_backchair = FieldTree(name="thickness_backchair", field=models.IntegerField(validators=[MinValueValidator(5),MaxValueValidator(12)]))
nbrods = FieldTree(name="nbrods", field=models.IntegerField(default=1,validators=[MinValueValidator(3),MaxValueValidator(10)]))
chairbacktype.add_subfield(parentChoice="flat", subfield=thickness_backchair)
chairbacktype.add_subfield(parentChoice="rods", subfield=nbrods)

length = FieldTree(name="length", field=models.FloatField)
width = FieldTree(name="width", field=models.FloatField)
height = FieldTree(name="height", field=models.FloatField)

root.add_subfield(parentChoice="Table", subfield=length)
root.add_subfield(parentChoice="Table", subfield=width)
root.add_subfield(parentChoice="Table", subfield=height)
root.add_subfield(parentChoice="Chair", subfield=height)
root.add_subfield(parentChoice="Chair", subfield=chairbacktype)

root.print()