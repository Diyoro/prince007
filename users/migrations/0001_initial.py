# Generated by Django 4.1.7 on 2023-03-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('date_naiss', models.DateField()),
                ('email', models.EmailField(max_length=50)),
                ('num_tel', models.CharField(max_length=10)),
            ],
        ),
    ]