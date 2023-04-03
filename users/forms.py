from .models import AdmitForm, AddTeacher
from django import forms

class AdmitForm(forms.ModelForm):
    """Form definition for AdmitForm."""

    class Meta:
        """Meta definition for AdmitFormform."""

        model = AdmitForm
        fields = ['nom', 'prenom', 'date_naiss', 'numero', 'email', 'genre', 'photo_prof']
    
    def __init__(self, *args,**kwargs):
        super(AdmitForm,self).__init__(*args,**kwargs)
        self.fields["nom"].widget.attrs ={"class": "col-xl-3 col-lg-6 col-12 form-group"}
        self.fields["prenom"].widget.attrs ={"class": "col-xl-3 col-lg-6 col-12 form-group"}
        self.fields["date_naiss"].widget.attrs ={"class": "col-xl-3 col-lg-6 col-12 form-group"}
        self.fields["numero"].widget.attrs ={"class": "col-xl-3 col-lg-6 col-12 form-group"}
        self.fields["genre"].widget.attrs ={"class": "col-xl-3 col-lg-6 col-12 form-group"}
        self.fields["photo_prof"].widget.attrs ={"class": "col-xl-3 col-lg-6 col-12 form-group"}
        self.fields["email"].widget.attrs ={"class": "col-xl-3 col-lg-6 col-12 form-group"}


class AddTeacher(forms.ModelForm):

    class Meta:
        model = AddTeacher
        fields =  ['nom', 'prenom', 'date_naiss', 'numero', 'email', 'genre', 'photo_prof']

    def __init__(self, *args, **kwargs):
        super(AddTeacher, self).__init__(*args, **kwargs)
      
