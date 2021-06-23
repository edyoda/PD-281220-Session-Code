from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return "{} {}".format(self.name, self.code)

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street_name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}, {}".format(self.street_name, self.city, self.postal_code)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE) # One to Many relations
    rating = models.IntegerField(default=0)
    is_bestselling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(Country, null=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.author)

    class Meta:
        db_table = "books"