from django.db import models

class Myhome(models.Model):

    
    image= models.ImageField(upload_to='skillimage/')
    title= models.CharField(max_length=50,blank=False)
    desc= models.TextField(max_length=500,blank=True)
    datetime= models.DateTimeField(auto_now_add=True)

    def summary(self):
         return self.desc[0:200]

    def __str__(self):
        return self.title

class Ideainfo(models.Model):
    iname = models.CharField(max_length=50)
    iemail = models.EmailField(max_length=50)
    iquery = models.TextField(max_length=1000)

    def __str__(self):
        return self.iname

class Branch(models.Model):
    bname = models.CharField(max_length=50)
    baddress = models.CharField(max_length=100)
    bphn1 = models.CharField(max_length=50)
    bphn2 = models.CharField(max_length=50)
    bspecialist1 = models.CharField(max_length=60)
    bspecialist2 = models.CharField(max_length=60)
    bseed = models.CharField(max_length=40)
    bfish = models.CharField(max_length=40)
    btrainingtime = models.CharField(max_length=50)

    def __str__(self):
        return self.bname
    
class Loan(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phn = models.CharField(max_length=50)
    branch = models.CharField(max_length=40)
    amount = models.FloatField(max_length=60)

    def __str__(self):
        return self.name

class ConfirmLoan(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    amount = models.FloatField(max_length=60)

    def __str__(self):
        return self.email
    

    