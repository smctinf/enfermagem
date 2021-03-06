# Generated by Django 3.2.7 on 2021-10-19 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0007_auto_20211018_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alocacao',
            options={'ordering': ['sala', 'candidato'], 'verbose_name': 'Alocação', 'verbose_name_plural': 'Alocações'},
        ),
        migrations.AlterModelOptions(
            name='horario',
            options={'ordering': ['local', 'horario'], 'verbose_name': 'Horário', 'verbose_name_plural': 'Horários'},
        ),
        migrations.AlterModelOptions(
            name='local',
            options={'ordering': ['nome'], 'verbose_name_plural': 'Locais'},
        ),
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selecao.candidato')),
            ],
            options={
                'ordering': ['dt_inclusao'],
            },
        ),
    ]
