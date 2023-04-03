from django.db import models
genre =(
    ('Masculin', 'Masculin'),
    ('Feminin', 'Feminin'),
    ('Autre', 'Autre')
)

class AdmitForm(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
    date_naiss = models.DateField()
    numero = models.CharField(max_length=10)
    email = models.EmailField()
    genre = models.CharField(max_length=10, choices=genre)
    photo_prof = models.ImageField(upload_to='media/profile_pictures/', default='profile_pic')

    def __str__(self):
        return self.nom

class AddTeacher(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
    date_naiss = models.DateField()
    numero = models.CharField(max_length=10)
    email = models.EmailField()
    genre = models.CharField(max_length=10, choices=genre)
    photo_prof = models.ImageField(upload_to='media/profile_pictures/', default='profile_pic')

    def __str__(self):
        return self.nom