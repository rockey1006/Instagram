"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Post(models.Model):
	"""Post model."""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)

	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100, unique=True, blank=True)
	photo = models.ImageField(upload_to='posts/photos')

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


	def __str__(self):
		"""Return title and username."""

		return '{} by @{}'.format(self.title, self.user.username)
