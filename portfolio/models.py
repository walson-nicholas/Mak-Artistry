from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    display_Img = models.ImageField(upload_to='images/', null=True)
    display_ImgTop = models.ImageField(upload_to='images/', null=True)
    display_ImgRight = models.ImageField(upload_to='images/', null=True)
    display_ImgLeft = models.ImageField(upload_to='images/', null=True)
    display_ImgRear = models.ImageField(upload_to='images/', null=True)
    size = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Illustration(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    display_Img = models.ImageField(upload_to='images/', null=True)
    display_ImgTop = models.ImageField(upload_to='images/', null=True)
    display_ImgRight = models.ImageField(upload_to='images/', null=True)
    display_ImgLeft = models.ImageField(upload_to='images/', null=True)
    display_ImgRear = models.ImageField(upload_to='images/', null=True)
    size = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Journal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    display_Img = models.ImageField(upload_to='images/', null=True)
    display_ImgTop = models.ImageField(upload_to='images/', null=True)
    display_ImgRight = models.ImageField(upload_to='images/', null=True)
    display_ImgLeft = models.ImageField(upload_to='images/', null=True)
    display_ImgRear = models.ImageField(upload_to='images/', null=True)
    size = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    display_Img = models.ImageField(upload_to='images/', null=True)
    display_ImgTop = models.ImageField(upload_to='images/', null=True)
    display_ImgRight = models.ImageField(upload_to='images/', null=True)
    display_ImgLeft = models.ImageField(upload_to='images/', null=True)
    display_ImgRear = models.ImageField(upload_to='images/', null=True)
    size = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
