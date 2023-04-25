from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request, 'sites/index.html')

def AccountSettings(request):
    return render(request, 'sites/account-settings.html')

def index3(request):
    return render(request, 'sites/index3.html')

def index4(request):
    return render(request, 'sites/index4.html')

def index5(request):
    return render(request, 'sites/index5.html')

def AllStudent(request):
    return render(request, 'sites/all-student.html')

def StudentDetails(request):
    return render(request, 'sites/student-details.html')

def AdmitForm(request):
    return render(request, 'sites/admit-form.html')

def StudentPromotion(request):
    return render(request, 'sites/student-promotion.html')

def AllTeacher(request):
    return render(request, 'sites/all-teacher.html')

def TeacherDetails(request):
    return render(request, 'sites/teacher-details.html')

def AddTeacher(request):
    return render(request, 'sites/add-teacher.html')

def TeacherPayment(request):
    return render(request, 'sites/teacher-payment.html')

def AllParents(request):
    return render(request, 'sites/all-parents.html')

def ParentsDetails(request):
    return render(request, 'sites/parents-details.html')

def AddParents(request):
    return render(request, 'sites/add-parents.html')

def AllBook(request):
    return render(request, 'sites/all-book.html')

def AddBook(request):
    return render(request, 'sites/add-book.html')

def AllFees(request):
    return render(request, 'sites/all-fees.html')

def AllExpense(request):
    return render(request, 'sites/all-expense.html')

def AddExpense(request):
    return render(request, 'sites/add-expense.html')

def AllClass(request):
    return render(request, 'sites/all-class.html')

def AddClass(request):
    return render(request, 'sites/add-class.html')

def AllSubject(request):
    return render(request, 'sites/all-subject.html')

def ClassRoutine(request):
    return render(request, 'sites/class-routine.html')

def StudentAttendence(request):
    return render(request, 'sites/student-attendence.html')

def login(request):
    return render(request,'sites/login.html' )


