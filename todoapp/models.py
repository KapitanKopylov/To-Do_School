from django.db import models


class TodoItem(models.Model):
	text = models.CharField(max_length=200, default=None)
	updated = models.DateTimeField(auto_now_add=True)
	completed = models.BooleanField(default=False, null=False)
	item_id = models.CharField(max_length=200, default='None')
	mail = models.CharField(max_length=200, default='None')

	class Meta:
		ordering = ['-updated']
	# def mail(self):
	# 	return self.mail
	

class TodoUsers(models.Model):
	mail = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
