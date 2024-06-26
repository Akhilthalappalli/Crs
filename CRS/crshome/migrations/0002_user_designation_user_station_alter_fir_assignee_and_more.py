# Generated by Django 4.0.1 on 2022-01-19 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crshome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, choices=[('DGP', 'DGP'), ('SI', 'SI'), ('CI', 'CI'), ('SP', 'SP'), ('ASP', 'ASP'), ('ASI', 'ASI'), ('CONSTABLE', 'CONSTABLE')], max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='station',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fir',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'ADMIN'), (2, 'PUBLIC'), (3, 'POLICE')], default=1),
        ),
        migrations.DeleteModel(
            name='Police',
        ),
    ]
