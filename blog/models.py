from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Post(models.Model):
	author=models.ForeignKey(User)
	title=models.CharField(max_length=50)
	text=models.TextField()
	create_date=models.DateTimeField(default=timezone.now)
	publish_date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.publish_date=timezone.now()
		self.save()
	def certified(self):
		return self.comments.filter(certified_comment=True)
	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'pk':self.pk})
	def __str__(self):
		return self.title
class Comment(models.Model):
	post=models.ForeignKey(Post,related_name="comments")
	author=models.CharField(max_length=50)
	text=models.TextField()
	create_date=models.DateTimeField(default=timezone.now)
	certified_comment=models.BooleanField(default=False)
	def approve_comment(self):
		self.certified_comment=True
		self.save()
	def get_absolute_url(self):
		return reverse('post_list')

	def __str__(self):
		return self.author


# Create your models here.
