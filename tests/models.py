from django.db import models


class Person(models.Model):
    age = models.PositiveIntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Document(models.Model):
    myfile = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.myfile.name if self.myfile else "No File"
