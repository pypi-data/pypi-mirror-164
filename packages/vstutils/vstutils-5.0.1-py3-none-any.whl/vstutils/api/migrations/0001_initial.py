# Generated by Django 2.2.2 on 2019-12-09 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [  # type: ignore
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
