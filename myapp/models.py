from django.db import models

# Create your models here.



class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True) 
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    email=models.CharField(max_length=250) #EmailField()
    phone_number=models.CharField(max_length=250)
    password=models.CharField(max_length=250)

class Patient(models.Model):
    patient_id=models.AutoField(primary_key=True) 
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    weight=models.FloatField(max_length=250)
    email=models.CharField(max_length=250)#EmailField()
    phone_number=models.CharField(max_length=250)
    password=models.CharField(max_length=250)

class Appointment(models.Model):
    appointment_id=models.AutoField(primary_key=True) 
    patient_id=models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor_id=models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    datetime=models.CharField(max_length=250)#DateTimeField()

class Prescription(models.Model):
    prescription_id=models.AutoField(primary_key=True) 
    pateient_id=models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor_id=models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    medicine=models.CharField(max_length=250)#TextField()
    date_created=models.CharField(max_length=250)#DateTimeField(auto_now_add=True)


