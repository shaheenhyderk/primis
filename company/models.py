from django.db import models


# Create your models here.
class Details(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=255)


class AptitudeQuestions(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    question = models.CharField(max_length=255)
    choice1 = models.CharField(max_length=255)
    choice2 = models.CharField(max_length=255)
    choice3 = models.CharField(max_length=255)
    choice4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=50)


class SpecificQuestions(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    question = models.CharField(max_length=255)
    choice1 = models.CharField(max_length=255)
    choice2 = models.CharField(max_length=255)
    choice3 = models.CharField(max_length=255)
    choice4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=50)


class JobOpenings(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    opening = models.CharField(max_length=255)
    company_id = models.CharField(max_length=50)


class QuestionIndex(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    job_opening_id = models.CharField(max_length=50)
    question_id = models.CharField(max_length=50)
