# Generated by Django 2.1.2 on 2018-11-12 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='nickname',
            field=models.CharField(default='嘿', max_length=100),
        ),
    ]
