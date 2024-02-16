# Generated by Django 5.0.1 on 2024-02-14 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABC_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='ABC_Customer',
        ),
        migrations.CreateModel(
            name='HR',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.employee')),
                ('salary', models.IntegerField()),
            ],
            bases=('first_app.employee',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.employee')),
                ('salary', models.IntegerField()),
            ],
            bases=('first_app.employee',),
        ),
    ]