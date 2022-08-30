from django.db import models

class ColoursToken(models.Model):
	token = models.TextField()
	daterandom = models.DateTimeField("Date random", auto_now_add = True)

	def __str__(self):
		return self.token
