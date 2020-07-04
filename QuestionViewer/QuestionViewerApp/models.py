from django.db import models
from django.urls import reverse
from .validator import validate_file_extension
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.FileField(upload_to='question', blank=True, validators=[validate_file_extension])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('dashboard', kwargs=None)



