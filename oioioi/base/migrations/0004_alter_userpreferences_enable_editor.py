# Generated by Django 3.2.13 on 2022-05-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220420_1236_squashed_0004_rename_preferred_language_userpreferences_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='enable_editor',
            field=models.BooleanField(default=False, verbose_name='enable_editor'),
        ),
    ]
