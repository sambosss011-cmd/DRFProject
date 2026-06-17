from .views import docList, docListUpdateDel ,patientList,patientUpdateDel, appointmentList, appointUpdateDel, prescriptionList, presUpdateDel
from django.urls import path
from . import views

urlpatterns=[
#   path("", views.home), 

 path('', docList, name='docList'),

 #path('doctor/<int:id>/', docList, name='docList'),

 #path("doctor/<int:id>/", views.docList)
 #path("PUT /doctor/{id}/",docList, name='docList'),

 #path("doctor/<int:id>/",docList, name='docList')

 # path("doctor/<int:id>/", views.docListUpdateDel)
 #path('doctor/<int:id>/',docListUpdateDel,name='docListUpdateDel')
#   path('doctor/<int:id>/', docListUpdateDel, name='doctor_update_delete'),

  path('update/<int:id>/', views.docListUpdateDel, name='update'),
  path('delete/<int:id>/', views.docListUpdateDel, name='delete'),

  path('p', patientList, name='patientList'),
  path('p/update/<int:id>/', views.patientUpdateDel, name='updatepatientList'),
  path('p/delete/<int:id>/', views.patientUpdateDel, name='updatepatientList'),

  path('a', appointmentList, name='appointmentList'),
  path('a/update/<int:id>/',views.appointUpdateDel, name='appointUpdateDel'),
  path('a/delete/<int:id>/',views.appointUpdateDel, name='appointUpdateDel'),

  path('pr', prescriptionList, name='prescriptionList'),
  path('pr/update/<int:id>/',views.presUpdateDel, name='presUpdateDel'),
  path('pr/delete/<int:id>/',views.presUpdateDel, name='presUpdateDel')

  


    
]
