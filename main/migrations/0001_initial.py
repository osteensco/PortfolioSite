# Generated by Django 4.0.5 on 2022-06-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relevance', models.IntegerField()),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('html', models.CharField(max_length=50)),
                ('relevance', models.IntegerField()),
                ('short_desc', models.CharField(max_length=280)),
                ('repo', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='')),
                ('technologies', models.ManyToManyField(to='main.technology')),
            ],
        ),
    ]
