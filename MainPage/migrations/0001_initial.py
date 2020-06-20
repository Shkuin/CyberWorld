# Generated by Django 3.0.5 on 2020-04-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=120)),
                ('preview_image', models.ImageField(upload_to='static/img')),
                ('text', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
    ]
