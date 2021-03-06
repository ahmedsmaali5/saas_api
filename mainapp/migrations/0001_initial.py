# Generated by Django 3.2 on 2021-12-16 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desciption', models.TextField(max_length=10000)),
                ('try_days', models.SmallIntegerField(default=7)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('Cost', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
