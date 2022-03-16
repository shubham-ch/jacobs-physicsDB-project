# Generated by Django 2.2 on 2022-03-16 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AddField(
            model_name='file',
            name='author',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='difficultyLevel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='fields',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='grading',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='intendedLearningOutcome',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='nameOfFile',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='nameOfLectures',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='purposeOfFile',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='sourceOfProblem',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='typeOfProblem',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='file',
            name='usedFor',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]