# Generated by Django 4.1.6 on 2023-02-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_ngo_email_remove_philanthropist_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='philanthropist',
            old_name='tax_exception_perc',
            new_name='fund_contrib',
        ),
        migrations.AddField(
            model_name='ngo',
            name='fund_received',
            field=models.IntegerField(null=True),
        ),
    ]
