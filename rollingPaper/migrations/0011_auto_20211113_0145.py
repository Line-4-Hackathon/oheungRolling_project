# Generated by Django 3.2.3 on 2021-11-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rollingPaper', '0010_auto_20211113_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rollinginfo',
            name='recipient_name',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='rollinginfo',
            name='rolling_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
