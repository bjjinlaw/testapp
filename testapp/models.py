from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title
    

class Status(models.TextChoices):
    TODO = "todo", "TODO"
    DOING = "doing", "DOING"
    DONE = "done", "DONE"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.TODO)


    def __str__(self):
        return self.title
