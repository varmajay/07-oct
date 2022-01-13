from django.db import models

# Create your models here.

class Seller(models.Model):

    doc_choice = (('pan','PAN Card '), ('aadhar','AAdhar Card'))

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile =  models.CharField(max_length=14)
    password = models.CharField(max_length=20)
    doc = models.CharField(max_length=20,choices=doc_choice)
    doc_number = models.CharField(max_length=20)
    address = models.TextField()
    verify = models.BooleanField(default=False)
    pic = models.FileField(upload_to='Profile',default='avtar.png')

    def __str__(self):
        return self.name + ' @  ' + self.email
