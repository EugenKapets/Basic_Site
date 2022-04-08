from django.db import models

class Task(models.Model):
    title = models.CharField("Name", max_length = 60)
    task = models.TextField("content")
   # author2 = models.TextField(default="anonim")
    def __str__(self):
        return self.title 
    class Meta:
       verbose_name = 'Task'
       verbose_name_plural = 'alltask'