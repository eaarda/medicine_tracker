# Generated by Django 3.1.6 on 2021-03-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=80)),
                ('dosage', models.IntegerField()),
                ('frequency', models.IntegerField()),
            ],
        ),
    ]
