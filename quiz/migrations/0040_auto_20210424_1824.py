# Generated by Django 3.0.3 on 2021-04-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0039_auto_20210424_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
