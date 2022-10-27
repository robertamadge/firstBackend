from unittest.util import _MAX_LENGTH
from django.db import models

class Class(models.Model):
    name_class = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name_class

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    name_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name