# Generated by Django 3.0.3 on 2021-04-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0028_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
