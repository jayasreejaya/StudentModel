# Generated by Django 4.2.1 on 2023-06-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Marks', models.FloatField()),
            ],
        ),
    ]
