# Generated by Django 5.0.2 on 2024-02-24 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_alter_contactsitem_id_user_alter_contactsitem_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsitem',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contactsitem',
            name='has_account',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contactsitem',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
