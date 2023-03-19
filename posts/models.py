from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
from tinymce import HTMLField

User = get_user_model()

class Author(models.Model):
	user = models.OneToOneField(User, default='None', on_delete=models.CASCADE)
	personal = models.TextField(max_length=100, default='None')
	handle = models.CharField(max_length=100, default='None')
	profile_picture = models.ImageField()


class Category(models.Model): 
	title = models.CharField(max_length=30)
	meta = models.TextField(max_length = 160, default='None')

	def __str__(self): 
		return self.title 



class Post(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	comment_count = models.IntegerField(default=0)
	view_count = models.IntegerField(default = 0)
	title = models.CharField(max_length = 100)
	thumbnail = models.ImageField()
	thumbnail_alt = models.TextField(default='A nice picture for the Pastel.Surf blog')
	categories = models.ManyToManyField(Category)
	meta = models.TextField(max_length = 160, default='None')
	featured = models.BooleanField()
	content = HTMLField()
	previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
	next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self): 
		return reverse('blog-post', kwargs={
			'id': self.id
		})
	@property
	def get_comments(self):
		return self.comments.all()


class Comment(models.Model): 
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username