# Generated by Django 4.0.5 on 2022-06-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='pdf',
            field=models.FileField(upload_to='static/'),
        ),
    ]
