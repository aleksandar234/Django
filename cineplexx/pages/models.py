from django.db import models

class Snippet(models.Model):
    question = models.CharField(max_length=100)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)

    def __str__(self):
        return self.question
