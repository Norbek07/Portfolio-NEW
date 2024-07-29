from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
    

class PortfolioItem(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='Images/portfolio')
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=50)



class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/blog')
    created_date = models.DateTimeField(auto_now=True)
    content = RichTextField()
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


class Comment(models.Model):
    full_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

class Gallery(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/gallery') 
    created_date = models.DateTimeField(auto_now=True)



class Books(models.Model):
    image = models.ImageField(upload_to='Images/books')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    pages = models.IntegerField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)


    def __str__(self):
        return self.title

class About(models.Model):
    image = models.ImageField(upload_to='Images/about', default='Images/about/default_image.jpg')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title