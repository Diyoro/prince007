from .views import AdmitFormCreateView, AddTeacherCreatView, listAdmitForm
from django.urls import path, include

urlpatterns = [
    path('create/', AdmitFormCreateView.as_view(),name="AdmitForm"),
    path('Diyoro/', AddTeacherCreatView.as_view(),name="AddTeacher"),
    path('listes/', listAdmitForm.as_view(),name="listAdmitForm")
]
