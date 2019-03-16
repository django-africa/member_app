from django.db import models

# Create your models here.

class Posts(models.Model):
	post_title=models.CharField(max_length=250)
	post_author=models.ForeignKey(auth.User, on_delete=models.CASCADE)
	published_date=models.DateTimeField(auto_now_add=True)
	post_body=models.TextField()
	image=models.FileField()

	def __str__(self):
		return self.post_title + '_' + self.post_author
