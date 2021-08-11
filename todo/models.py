from django.db import models

# Create your models here.

CHOICE = ('denger', 'high'), ('warning', 'normal'), ('primary', 'low')


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=CHOICE
    )
    duedate = models.DateTimeField()

    def __str__(self):
        return self.title
