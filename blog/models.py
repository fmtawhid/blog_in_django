from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class auth(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='pro_pic')
    details = models.TextField(max_length=200)

    def __str__(self):
        return self.name.username


class catagory(models.Model):
    catagory_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.catagory_name


class article(models.Model):
    article_auth = models.ForeignKey(auth, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(max_length=300)
    image = models.FileField(upload_to='post')
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)


    def __str__(self):
        return self.title