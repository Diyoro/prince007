# Generated by Django 4.1.7 on 2023-03-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_admitform_photo_prof'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=50)),
                ('date_naiss', models.DateField()),
                ('numero', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('genre', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin'), ('Autre', 'Autre')], max_length=10)),
                ('photo_prof', models.ImageField(default='profile_pic', upload_to='media/profile_pictures/')),
            ],
        ),
    ]
