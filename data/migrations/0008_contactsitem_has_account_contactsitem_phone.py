# Generated by Django 5.0.2 on 2024-02-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_addtaskitem_subtask'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactsitem',
            name='has_account',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AddField(
            model_name='contactsitem',
            name='phone',
            field=models.IntegerField(default=0, verbose_name=''),
        ),
    ]
