from django.db import models

# Create your models here.
class Student(models.Model):
    Roll_no=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    Marks=models.FloatField()
    def __str__(self):
        return  str(self.Roll_no)
