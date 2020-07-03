from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=11,primary_key=True)
    bank_id= models.IntegerField()
    branch=models.CharField(max_length=74)
    address=models.CharField(max_length=195)
    city=models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state=models.CharField(max_length=26)
    name=models.CharField(max_length=49)

    def __str__(self):
        return self.name