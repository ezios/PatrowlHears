# Generated by Django 3.0.10 on 2020-10-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cves', '0004_auto_20200730_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cve',
            name='summary',
            field=models.TextField(blank=True, default=''),
        ),
    ]