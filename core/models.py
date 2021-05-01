from django.db import models

# Create your models here.
class Post(models.Model):
    category = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(blank=True, default='default.jpg', upload_to = 'media/')
    date_added = models.DateTimeField(auto_now_add=True)
    intro = models.TextField()
    body = models.TextField()
    
    
    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ['-date_added']
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE) 
    name = models.TextField(max_length=200)
    body = models.TextField()  
    date_added = models.DateTimeField(auto_now_add=True)                       
    
    class Meta:
        ordering = ['date_added']
        
class Prediction(models.Model):
    slug = models.SlugField()    
    teams = models.TextField()
    tip = models.CharField(max_length=200)
    odd = models.CharField(max_length=200)
