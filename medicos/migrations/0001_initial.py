# Generated by Django 4.0.6 on 2022-07-30 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('crm', models.IntegerField(unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
