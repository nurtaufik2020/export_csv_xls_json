from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=220)
    description=models.TextField()
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    # def __str__(self):
    #     return str(self.title)
