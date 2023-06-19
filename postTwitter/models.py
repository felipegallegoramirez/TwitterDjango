from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    def __str__(self):
        # Esto permite que en el admin se vea el nombre
        return self.name
    
class userPost(models.Model):
    content= models.CharField(max_length=320)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    def __str__(self):
        return self.content[0:20] + '... - ' + self.user.name