# Generated by Django 3.2.4 on 2021-06-21 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0005_auto_20210621_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]
