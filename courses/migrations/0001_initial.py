# Generated by Django 4.1.7 on 2023-04-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=250)),
                ('category', models.ManyToManyField(to='courses.categories')),
            ],
        ),
    ]
