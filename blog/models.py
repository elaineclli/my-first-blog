from django.conf import settings
from django.db import models
from django.utils import timezone

#class 				indicates that we are defining an object.
#Post 				is the name of our model, always start a class name with an uppercase letter.
#models.Model		means that the Post is a Django Model, so Django knows that it should be saved in the database.

#Python is sensitive to whitespace, we need to indent our methods inside the class

class Post(models.Model):
	author 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title 			= models.CharField(max_length=200)
	text 			= models.TextField()
	created_date 	= models.DateTimeField(default=timezone.now)
	published_date	= models.DateTimeField(blank=True, null=True)
	
	#def 		this is a function/method
	#publish	method name, use lowercase and underscores instead of spaces
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title