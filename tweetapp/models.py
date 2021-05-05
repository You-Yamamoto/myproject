from django.db import models
from profiles.models import Profile
class BoardModel(models.Model):
		title = models.CharField(max_length = 100)
		content = models.TextField()
		author = models.ForeignKey(Profile, on_delete = models.CASCADE)
		snsimage = models.ImageField(upload_to = '')
		good = models.IntegerField(null=True, blank=True ,default=1)
		read = models.IntegerField(null=True, blank=True , default = 1)
		readtext = models.TextField(null=True, blank=True , default= 'a')
		update = models.DateTimeField(auto_now= True)
		created = models.DateTimeField(auto_now_add= True)

		def __str__(self):
				return str(self.content)[:30]

		class Meta:
				ordering = ('-created',)
