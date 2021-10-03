# Generated by Django 3.2.7 on 2021-10-03 16:04

from django.db import migrations, models
import selecao.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('dt_nascimento', models.DateField(verbose_name='Data Nascimento')),
                ('cpf', models.CharField(max_length=11, unique=True, validators=[selecao.functions.validate_CPF])),
                ('tel', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('deficiencia', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1)),
                ('qual_deficiencia', models.CharField(max_length=200)),
                ('necessidade', models.CharField(max_length=200)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
