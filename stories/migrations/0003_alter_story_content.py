# Generated by Django 4.0 on 2022-01-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_alter_story_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=models.TextField(blank=True, help_text='Describe the story. This field is optional.'),
        ),
    ]
