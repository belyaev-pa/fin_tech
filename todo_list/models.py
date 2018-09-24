from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{}'.format(self.name)