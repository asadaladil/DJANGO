from django.db import models

# Create your models here.
class ToDoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=30)
    is_completed = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.title