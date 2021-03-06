# Generated by Django 3.2.7 on 2021-10-18 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0006_candidato_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['local', 'horario'],
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('rua', models.CharField(max_length=60)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(max_length=5)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.horario')),
            ],
            options={
                'ordering': ['horario', 'sala'],
            },
        ),
        migrations.AddField(
            model_name='horario',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.local'),
        ),
        migrations.CreateModel(
            name='Alocacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.candidato')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.sala')),
            ],
            options={
                'ordering': ['sala', 'candidato'],
            },
        ),
    ]
