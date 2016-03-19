from django.db import models

class Post(models.Model):
	title = models.CharField()
	body = models.TextFiel()
	date = models.DateTimeField()