from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Articles(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	auther = models.CharField(max_length=120, default='ibirdi')
	path = models.CharField(max_length=120, default='icharan')
	imgpath = models.CharField(max_length=120, default='icharan')
	topic = models.CharField(max_length=120, default='Transformer')
	html = models.TextField(default= '<p>yooo</p>')


	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title



	class Meta:
		ordering = ["-timestamp", "-updated"]
