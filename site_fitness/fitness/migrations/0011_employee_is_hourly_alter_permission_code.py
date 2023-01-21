# Generated by Django 4.1.4 on 2023-01-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0010_client_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_hourly',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]