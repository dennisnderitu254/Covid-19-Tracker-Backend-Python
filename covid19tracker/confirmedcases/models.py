from django.db import models

class ConfirmedCase(models.Model):
    date_reported = models.DateField()
    cases = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.date_reported} - {self.cases} cases"

