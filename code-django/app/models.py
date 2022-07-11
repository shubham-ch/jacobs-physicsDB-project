from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class file(models.Model):
    id = models.BigAutoField(primary_key=True)
    nameOfFile = models.CharField(max_length=150, blank=True)
    nameOfLectures = models.CharField(max_length=150, blank=True)
    # subject fields
    fields = models.CharField(max_length=150, blank=True)
    file_upload = models.FileField(null=True, blank=True, upload_to="media/")
    # availability for extercises
    usedFor = models.CharField(max_length=150, blank=True)
    difficultyLevel = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True)
    # from where the problem is derived
    sourceOfProblem = models.CharField(max_length=150, blank=True)
    author = models.CharField(max_length=150, blank=True)
    # numerical, theoritical e.t.c
    typeOfProblem = models.CharField(max_length=150, blank=True)
    intendedLearningOutcome = models.CharField(max_length=150, blank=True)
    # purpose for example exam, homework
    purposeOfFile = models.CharField(max_length=150, blank=True)
    grading = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nameOfFile

    # to connect to a foreign table in case of one to one use
    # name = models.ForeignKey(name of table/class, blank=True, null=True, on_delete=models.CASCADE)

    # for many to many field to connect two tables
    # name = models.ManyToManyField(name of table/class, blank=True)
