from django.db import models


# Create your models here.
class PersonalDetails(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    job_opening_id = models.CharField(max_length=50)
    project = models.CharField(max_length=255)
    why_hire_you = models.TextField()
    status = models.CharField(max_length=50)
    aptitude_result = models.IntegerField()
    skill_result = models.IntegerField()
    total_result = models.IntegerField()


class AptitudeResult(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user_id = models.CharField(max_length=50)
    question_id = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    correct = models.BooleanField()


class SkillResult(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    user_id = models.CharField(max_length=50)
    question_id = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.CharField(max_length=50)
    correct = models.BooleanField()

