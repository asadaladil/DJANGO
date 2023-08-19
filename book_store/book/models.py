from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY=(
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Sci-fi','Sci-fi'),
        ('Humor','Humor'),
        ('Horor','Horor'),
    )
    id = models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    category=models.CharField(max_length=30,choices=CATEGORY)
    first_pub=models.DateTimeField(auto_now_add=True) #first date no change when updating
    last_pub=models.DateTimeField(auto_now=True) #change in updating