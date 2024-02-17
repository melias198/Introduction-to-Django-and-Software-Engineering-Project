# Generated by Django 5.0.1 on 2024-02-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStoreModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Sci-Fi', 'Sci-Fi'), ('Romantic', 'Romantic'), ('Islamic', 'Islamic'), ('Humor', 'Humor'), ('Horror', 'Horror')], max_length=30)),
                ('page', models.IntegerField()),
                ('price', models.IntegerField()),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateTimeField()),
            ],
        ),
    ]