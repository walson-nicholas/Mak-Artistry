from django.db import models


class WhatsNew(models.Model):
    display_Img = models.ImageField(upload_to='images/', null=True)
    writeUp = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        

class WhatWeDo(models.Model):
    display_Img = models.ImageField(upload_to='images/', null=True)
    writeUp = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        
class CustomersReview(models.Model):
    display_Img = models.ImageField(upload_to='images/', null=True)
    writeUp = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']