from .views import AdmitFormCreateView, AddTeacherCreatView
from django.urls import path, include

urlpatterns = [
    path('create/', AdmitFormCreateView.as_view(),name="AdmitForm"),
    path('Diyoro/', AddTeacherCreatView.as_view(),name="AddTeacher"),
]
