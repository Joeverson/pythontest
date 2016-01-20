from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class news(models.Model):

	title = models.CharField(max_length=200)
	descriptin = models.CharField(max_length=255)
	content = models.TextField()
	author = models.ForeignKey(User)
	image = models.CharField(max_length=200, blank=True, null=True)


	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

