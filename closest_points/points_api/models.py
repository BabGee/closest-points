from django.db import models


class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return f'{self.x},{self.y}'
