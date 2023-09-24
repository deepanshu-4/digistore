from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=500)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=122)
    phoneno=models.CharField(max_length=12)
    date=models.DateField()
    def __str__(self):
        return self.name+" "+self.email
        
class video(models.Model):
    username=models.CharField(max_length=500)
    video=models.CharField(max_length=500)
    def __str__(self):
        return self.username
class Post(models.Model):
    title = models.CharField(max_length=250)
    guser = models.CharField(max_length=250)
    # description = models.TextField()
    # image = models.FileField(blank=True)

    def __str__(self):
        return self.title+" "+self.guser

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title

#for music
class pPost(models.Model):
    title = models.CharField(max_length=250)
    guser = models.CharField(max_length=250)
    # description = models.TextField()
    # image = models.FileField(blank=True)

    def __str__(self):
        return self.title+" "+self.guser

class Postpdf(models.Model):
    post = models.ForeignKey(pPost, default=None, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to = 'files/',blank=True, storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return self.post.title

#for files
class fpPost(models.Model):
    title = models.CharField(max_length=250)
    guser = models.CharField(max_length=250)
    # description = models.TextField()
    # image = models.FileField(blank=True)

    def __str__(self):
        return self.title+" "+self.guser

class fPostpdf(models.Model):
    post = models.ForeignKey(fpPost, default=None, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to = 'filepdf/',blank=True, storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return self.post.title

#for home page
class listing(models.Model):
    puser=models.CharField(max_length=2000)
    image = models.FileField(upload_to = 'files/')
    like = models.CharField(max_length=2000)
    dislike=models.CharField(max_length=2000)