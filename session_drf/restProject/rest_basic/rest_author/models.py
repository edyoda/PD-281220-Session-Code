from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} By - {}".format(self.title, self.author)