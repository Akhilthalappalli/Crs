# Generated by Django 4.0.1 on 2022-01-22 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crshome', '0003_remove_user_phone_code_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]