from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from .models import AddTeacher, AdmitForm
from .forms import AdmitForm as AdForm, AddTeacher as AdTeacher
from django.views.generic.edit import CreateView
# Create your views here.


def AdmitForm(request):
    objets = AdmitForm.objects.all()
    return render(request,'sites/admit-form.html', {'objets':objets} )


class AdmitFormCreateView(CreateView):
    model = AdmitForm
    form_class = AdForm
    template_name = "sites/admit-form.html"
    success_url = reverse_lazy('index')


def AddTeacher(request):
    objets = AddTeacher.objects.all()
    return render(request, 'sites/AddTeacher.html', {'objets':objets} )


class AddTeacherCreatView(CreateView):
    model = AddTeacher
    form_class = AdTeacher
    template_name = "sites/add-teacher.html"
    success_url = reverse_lazy('AddTeacher')