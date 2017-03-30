from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Event(models.Model):
	event_name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	host = models.ForeignKey('users.User', related_name = "for_host", on_delete=models.CASCADE, default = None,)
	description = models.TextField()
	longitude = models.CharField(max_length=255)
	latitude = models.CharField(max_length=255)

	def __str__(self):
		return self.event_name
