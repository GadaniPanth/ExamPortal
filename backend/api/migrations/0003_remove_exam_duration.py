# Generated by Django 5.0.8 on 2024-09-23 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_question_option1_question_option2_question_option3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='duration',
        ),
    ]