# Generated by Django 4.1.7 on 2023-07-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_memories_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='notification',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
