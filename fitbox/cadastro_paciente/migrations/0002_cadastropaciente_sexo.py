# Generated by Django 3.1.2 on 2020-10-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_paciente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastropaciente',
            name='sexo',
            field=models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino']], max_length=1, null=True),
        ),
    ]
