# Generated by Django 3.0.3 on 2021-04-20 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0034_auto_20210420_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Course',
            new_name='course',
        ),
        migrations.AddField(
            model_name='subject',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Branch'),
        ),
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Course'),
        ),
        migrations.AddField(
            model_name='subject',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.School'),
        ),
        migrations.AddField(
            model_name='subject',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Section'),
        ),
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Year'),
        ),
    ]
