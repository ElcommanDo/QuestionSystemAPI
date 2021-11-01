from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='questions')

    def __str__(self):
        return self.content


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    voters = models.ManyToManyField(User, related_name='votes')

    def __str__(self):
        return self.body


