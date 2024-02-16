# Generated by Django 5.0.1 on 2024-02-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_abc_employee_remove_employee_salary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=10)),
                ('present', models.BooleanField()),
                ('hw', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('first_app.friend',),
        ),
    ]