# Generated by Django 4.1.7 on 2023-03-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_admitform_delete_etudiant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admitform',
            name='photo_prof',
            field=models.ImageField(default='profile_pic', upload_to='media/profile_pictures/'),
        ),
    ]
