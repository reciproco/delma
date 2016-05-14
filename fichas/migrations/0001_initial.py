# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import fichas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('fichero', models.FileField(upload_to=fichas.models.path_and_rename)),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesion', models.CharField(max_length=1024)),
                ('cuando', models.DateTimeField()),
                ('como', models.CharField(max_length=1024)),
                ('tratamiento_ee', models.BooleanField(default=False)),
                ('tratamiento_ir', models.BooleanField(default=False)),
                ('tratamiento_tm', models.BooleanField(default=False)),
                ('tratamiento_us', models.BooleanField(default=False)),
                ('tratamiento_l', models.BooleanField(default=False)),
                ('tratamiento_mg', models.BooleanField(default=False)),
                ('tratamiento_cines', models.BooleanField(default=False)),
                ('tratamiento_synm', models.BooleanField(default=False)),
                ('tratamiento_tc', models.BooleanField(default=False)),
                ('tratamiento_ps', models.BooleanField(default=False)),
                ('tratamiento_epte', models.BooleanField(default=False)),
                ('observaciones', models.TextField()),
                ('terapeuta', models.CharField(choices=[('ALB', 'ALBERTO'), ('DEL', 'DELFIN'), ('CAR', 'CAROLINA')], default='ALB', max_length=3)),
                ('dolor', models.CharField(max_length=128)),
                ('sesiones', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido1', models.CharField(max_length=32)),
                ('apellido2', models.CharField(max_length=32)),
                ('direccion', models.CharField(max_length=512)),
                ('telefono', models.CharField(max_length=32)),
                ('correo', models.EmailField(max_length=254)),
                ('dni', models.CharField(max_length=16)),
                ('nacimiento', models.DateTimeField()),
                ('alta', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='ficha',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='fichas.Paciente'),
        ),
        migrations.AddField(
            model_name='adjunto',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.Ficha'),
        ),
    ]
