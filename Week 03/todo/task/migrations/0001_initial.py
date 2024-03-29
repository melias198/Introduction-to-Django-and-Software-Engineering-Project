# Generated by Django 5.0.1 on 2024-02-17 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.TextField(max_length=100)),
                ('taskDescription', models.TextField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
