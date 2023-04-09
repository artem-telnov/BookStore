import datetime
from django.db import models


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    birth_date = models.DateField(blank=False, default=datetime.datetime.now)
    is_alive = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
