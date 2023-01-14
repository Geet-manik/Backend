from django.db import models
# Create your models here.
class meeting (models.Model):
    Serial= models.IntegerField(null=True)
    Subject=models.CharField(max_length=122)
    Format=models.CharField(max_length=122)
    Date=models.DateField(null=True)

class ugSenator(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Image=models.ImageField(upload_to="")

    def _str_(self):
       return self.Position
class pgSenator(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def _str_(self):
       return self.Position


class facultyExecutivebodie(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def _str_(self):
       return self.Position
class studentExecutivebodie(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def _str_(self):
       return self.Position                     

class upcomingEvent(models.Model):
    Description=models.CharField(max_length=500)
  
    Image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def _str_(self):
       return self.Position                     
   