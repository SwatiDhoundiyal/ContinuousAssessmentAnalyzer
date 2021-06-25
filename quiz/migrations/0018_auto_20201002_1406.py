# Generated by Django 3.0.3 on 2020-10-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_auto_20201002_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Answer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='Option1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='Option2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='Option3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='Option4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='Question_Text',
            field=models.CharField(max_length=500),
        ),
    ]