# Generated by Django 2.2.1 on 2019-07-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qgisfeed', '0003_auto_20190518_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qgisfeedentry',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to='feedimages/%Y/%m/%d/', verbose_name='Image', width_field='image_width'),
        ),
        migrations.AlterField(
            model_name='qgisfeedentry',
            name='publish_to',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Publication end'),
        ),
    ]
