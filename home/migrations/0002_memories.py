# Generated by Django 4.1.7 on 2023-04-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('video', models.FileField(upload_to='Associations')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]