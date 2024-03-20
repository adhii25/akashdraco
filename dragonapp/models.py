from django.db import models

# Create your models here.
class Categories(models.Model):
    category=models.CharField(max_length=30,unique=True)
    slug=models.SlugField()

    def __str__(self):
        return self.category


class Movies(models.Model):
    movie=models.CharField(max_length=30,unique=True)
    release_date=models.DateField()
    description=models.TextField()
    poster=models.ImageField(upload_to="posters")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    links = models.SlugField()
    websites = models.URLField(max_length=200)
    actors = models.TextField(blank=True)

    def __str__(self):
        return self.movie

    class Meta:
        verbose_name="Movie"
        verbose_name_plural="Movies"