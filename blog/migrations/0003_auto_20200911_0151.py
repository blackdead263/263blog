# Generated by Django 3.0.8 on 2020-09-11 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200911_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='dump', max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
