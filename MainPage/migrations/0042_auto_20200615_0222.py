# Generated by Django 3.0.5 on 2020-06-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0041_auto_20200604_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(default='android.png', null=True, upload_to=''),
        ),
    ]
