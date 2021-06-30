from django.db import models


class TimeStampedModelMixin(models.Model):
    created_at = models.DateTimeField('Создано в', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено в', auto_now=True)

    class Meta:
        abstract = True
