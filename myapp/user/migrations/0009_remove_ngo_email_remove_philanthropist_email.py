# Generated by Django 4.1.6 on 2023-02-11 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_ngo_review_likes_philanthropist_primary_cause_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='philanthropist',
            name='email',
        ),
    ]
