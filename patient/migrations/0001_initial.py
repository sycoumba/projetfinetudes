# Generated by Django 3.2 on 2021-04-10 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=150)),
                ('age', models.TextField(null=True)),
                ('sexe', models.TextField(null=True)),
                ('adresse', models.TextField()),
            ],
        ),
    ]
