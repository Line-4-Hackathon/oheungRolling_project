# Generated by Django 3.2.3 on 2021-11-12 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rollingPaper', '0005_auto_20211113_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rollinginfo',
            name='comment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rollingPaper.comment'),
        ),
    ]
