from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("modified at"), auto_now=True)

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email if self.email else self.username

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class NeedRessource(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class NeedType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Need(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    exclude_from_storage = models.BooleanField(default=False)
    capacity_factor = models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    needs_type = models.ForeignKey(NeedType, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NeedValue(models.Model):
    value = models.CharField(max_length=200)
    hour_start = models.DateTimeField(blank=True)
    hour_end = models.DateTimeField(blank=True)
    day_start = models.IntegerField(blank=True)
    day_end = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    need = models.ForeignKey(Need, on_delete=models.CASCADE)

    def __str__(self):
        return self.value


class MaterialType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MaterialCustomField(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MaterialCustomFieldValue(models.Model):
    value = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.value
