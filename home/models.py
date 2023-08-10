from django.db import models
from datetime import date

class County(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # Add other fields for county information

    def __str__(self):
        return self.name
    
class Subcounty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='subcounties')
    

    def __str__(self):
        return self.name
    
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Subcounty, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    dob = models.DateField()
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='students_county', default='')
    subcounty = models.ForeignKey(Subcounty, on_delete=models.PROTECT, related_name='students_subcounty', default='')
    parent_guardian_id = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other')

    @property
    def age(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

    def __str__(self):
        return self.student_name



