from django.db import models
import copy

class FieldTree:
    def __init__(self,name, field):

        self.name = name
        self.field = field

        self.subfields = []
        self.parentKey = None
        self.choices = None
        if isinstance(field,models.CharField):
            pass

    def add_subfield(self,parentKey, subfield):
        subfield = copy.copy(subfield)
        subfield.parentKey = parentKey
        self.subfields.append(subfield)

    def print(self):
        print(self.parentKey, self.name)
        for subfield in self.subfields:
            subfield.print()


root = FieldTree(name="type", field=models.CharField(max_length=100,choices=(("Chair","Chaise"),("Table","Table"))))

length = FieldTree(name="length", field=models.FloatField)
width = FieldTree(name="width", field=models.FloatField)
height = FieldTree(name="height", field=models.FloatField)

root.add_subfield(parentKey="Table", subfield=length)
root.add_subfield(parentKey="Table", subfield=width)
root.add_subfield(parentKey="Table", subfield=height)
root.add_subfield(parentKey="Chair", subfield=height)

root.print()

