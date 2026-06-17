from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctor, Patient ,Appointment ,Prescription
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, PrescriptionSerializer


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
@api_view()
def home(request):
    return Response({"message": "Hi all welcome to LGS..."})

#For Doctor model CRUD Operations ; Similarly we have to make separate CRUD opaertions for Patient
#Appointment, Prescription models in views.py i.e., GET,POST,PUT,DELETE for each Patient, Appointment
#Prescription each one of them in views.py

#Never forget to include in "Myproject urls" - myapp (include it)

#Never forget to register endpoints of all GET,POST,PUT,DELETE in "myapp urls"

@api_view(["GET", "POST"])
def docList(request):
    if request.method=="GET":
        queryset=Doctor.objects.all()
        serializer=DoctorSerializer(queryset, many=True)

        #return Response({"docList":serializer.data})
        return Response(serializer.data)

    elif request.method=="POST":
        value=request.data
        serializer=DoctorSerializer(data=value)

        if serializer.is_valid():
            serializer.save()
            #return Response("Doctor added successfully!")
            #return Response( {"message": "Doctor added successfully!", "data": serializer.data})
            return Response(serializer.data)

        return Response(serializer.errors)

#######Make PUT and DELETE Functionality for Doctor's CRUD OPeration###########





@api_view(["PUT", "DELETE"])
def docListUpdateDel(request, id):
    try:
        doctor = Doctor.objects.get(doctor_id=id)
    except Doctor.DoesNotExist:
        return Response({"error": "Doctor not found"}, status=404)

    # UPDATE
    if request.method == "PUT":
        serializer = DoctorSerializer(doctor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Doctor updated successfully!",
                "data": serializer.data
            })
        return Response(serializer.errors, status=400)

    # DELETE
    if request.method == "DELETE":
        doctor.delete()
        return Response({"message": "Doctor deleted successfully!"})

@api_view(["GET", "POST"])
def patientList(request):
     if request.method=="GET":
        queryset=Patient.objects.all()
        
        serializer=PatientSerializer(queryset, many=True)
        return Response(serializer.data)

     elif request.method=="POST":
        value=request.data
        serializer=PatientSerializer(data=value)

        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.data)

        return Response(serializer.errors)

@api_view(["PUT", "DELETE"])
def patientUpdateDel(request, id):
    try:
        patient=Patient.objects.get(patient_id=id)
    except Patient.DoesNotExist: 
        return Response({"error":"Patient Not Found"},status=404)

#update
    if request.method=="PUT":
        serializer=PatientSerializer(Patient, data=request.data)
        if serializer.is_valid():
            #serializer.save()
            serializer.save()
           

        return Response({
                "message": "Patient updated successfully",
                    "data": serializer.data

        })
        return Response(serializer.errors, status=400)

#delete
    if request.method == "DELETE":
            patient.delete()
            return Response({"message": "Patient deleted successfully!"})


@api_view(["GET", "POST"])
def appointmentList(request):
    if request.method=="GET":
        queryset=Appointment.objects.all()
        serializer=AppointmentSerializer(queryset,many=True)

        return Response(serializer.data)

    elif request.method=="POST":
        value=request.data
        serializer=AppointmentSerializer(data=value)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["PUT","DELETE"])
def appointUpdateDel(request,id):
    try:
        appointment=Appointment.objects.get(appointment_id=id)
    except Appointment.DoesNotExist:
        return Response({"error":"Appointment not found"},status=404)

#update
    if request.method=="PUT":
        serializer=AppointmentSerializer(appointment, data= request.data)

        if serializer.is_valid():
            serializer.save()

        return Response({"message":"Appointment Updated",
                          "data": serializer.data})

        return Response(serializer.errors, status=400)

#delete
    if request.method=="DELETE":
        appointment.delete()
    return Response({"message":"Appointment Deleted successfully"})

@api_view(["GET", "POST"])
def prescriptionList(request):
    if request.method=="GET":
        queryset=Prescription.objects.all()
        serializer=PrescriptionSerializer(queryset, many=True)

        return Response(serializer.data)

    elif request.method=="POST":
        value=request.data
        serializer=PrescriptionSerializer(data=value)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

        return Response (serializer.errors)

@api_view(["PUT","DELETE"])
def presUpdateDel(request,id):
    try:
        prescription=Prescription.objects.get(prescription_id=id)
    except Prescription.DoesNotExist:
        return Response({"error":"Prescription not found"},status=404)

#update
    if request.method=="PUT":
        serializer=PrescriptionSerializer(prescription, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response({
            "message":"Prescription Updated",
            "data":serializer.data
        })

        return Response(serilaizer.errors, status=400)

#delete
    if request.method=="DELETE":
        prescription.delete()
    return Response({"message":"Prescription Deleted successfully"})

    ###########################################################################

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None):
#     content = {
#         'user': str(request.user),  # `django.contrib.auth.User` instance.
#         'auth': str(request.auth),  # None
#     }
#     return Response(content)



        








