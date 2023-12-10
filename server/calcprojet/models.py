from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by_email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MaterialType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by_email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MaterialCustomField(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by_email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MaterialCustomFieldValue(models.Model):
    value = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by_email = models.CharField(max_length=200)

    def __str__(self):
        return self.value

