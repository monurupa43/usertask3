from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    dob= models.DateField()

    def __str__(self):
        return self.name

# Create your models here.
