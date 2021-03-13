from django.db import models


class Project(models.Model):
	owner = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	description = models.TextField()
	

class Task(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
