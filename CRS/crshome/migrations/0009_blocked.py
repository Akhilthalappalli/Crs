# Generated by Django 4.0.1 on 2022-01-23 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crshome', '0008_complaint_name_complaint_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13)),
            ],
        ),
    ]