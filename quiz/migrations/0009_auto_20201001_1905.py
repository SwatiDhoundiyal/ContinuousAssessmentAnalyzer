# Generated by Django 3.0.3 on 2020-10-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20201001_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Answer',
            field=models.CharField(default=models.CharField(max_length=100, null=True), max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='Option1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Option2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
