# Generated by Django 3.1.2 on 2020-10-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32)),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sexo', models.CharField(choices=[['F', 'Feminino'], ['M', 'Masculino']], max_length=1, null=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=32)),
            ],
        ),
    ]
