# Generated by Django 3.2.13 on 2022-05-31 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0004_alter_reservation_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='events',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='gallery',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cell',
            field=models.CharField(default=0, max_length=15),
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menu',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant/menu'),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.DeleteModel(
            name='ItemMenu',
        ),
    ]
