# Generated by Django 5.0.1 on 2024-02-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='taskTitle',
            field=models.CharField(max_length=50),
        ),
    ]
