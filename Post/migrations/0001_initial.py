# Generated by Django 3.1.7 on 2021-04-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('nameOfPoster', models.CharField(max_length=100)),
                ('nameOfLocation', models.CharField(max_length=100)),
                ('photoURL', models.TextField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
