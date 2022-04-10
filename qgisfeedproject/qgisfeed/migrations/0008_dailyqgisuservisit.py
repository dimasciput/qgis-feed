# Generated by Django 4.0.3 on 2022-04-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qgisfeed', '0007_qgisuservisit'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyQgisUserVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('qgis_version', models.JSONField()),
                ('platform', models.JSONField()),
                ('country', models.JSONField()),
            ],
        ),
    ]
