# Generated by Django 4.0.4 on 2022-05-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
