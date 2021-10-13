from django.db import models

# Create your models here.

class PortfolioProject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    media = models.FileField()