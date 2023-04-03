from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('AccountSettings/', AccountSettings, name='AccountSettings'),
    path('index3/', index3, name='index3'),
    path('index4/', index4, name='index4'),
    path('index5/', index5, name='index5'),
    path('AllStudent/', AllStudent, name='AllStudent'),
    path('StudentDetails/', StudentDetails, name='StudentDetails'),
    path('AdmitForm/', AdmitForm, name='AdmitForm'),
    path('StudentPromotion/', StudentPromotion, name='StudentPromotion'),
    path('AllTeacher/', AllTeacher, name='AllTeacher'),
    path('TeacherDetails/', TeacherDetails, name='TeacherDetails'),
    path('AddTeacher/', AddTeacher, name='AddTeacher'),
    path('TeacherPayment/', TeacherPayment, name='TeacherPayment'),
    path('AllParents/', AllParents, name='AllParents'),
    path('ParentsDetails/', ParentsDetails, name='ParentsDetails'),
    path('AddParents/', AddParents, name='AddParents'),
    path('AllBook/', AllBook, name='AllBook'),
    path('AddBook/', AddBook, name='AddBook'),
    path('AllFees/', AllFees, name='AllFees'),
    path('AllExpense/', AllExpense, name='AllExpense'),
    path('AddExpense/', AddExpense, name='AddExpense'),
    path('AllClass/', AllClass, name='AllClass'),
    path('AddClass/', AddClass, name='AddClass'),
    path('AllSubject/', AllSubject, name='AllSubject'),
    path('ClassRoutine/', ClassRoutine, name='ClassRoutine'),
    path('StudentAttendence/', StudentAttendence, name='StudentAttendence'),
]

