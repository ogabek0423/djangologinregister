# Generated by Django 5.0.3 on 2024-03-23 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_coursesrecord_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='media/users/')),
                ('shior', models.TextField()),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.coursespeciality')),
            ],
        ),
    ]
