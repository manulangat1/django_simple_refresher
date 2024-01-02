import uuid

from django.db import models

# Create your models here.


class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False, db_index=True)
    id = models.UUIDField(
        default=uuid.uuid4(), editable=False, unique=True, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # verbose_name = "TimeStampedUUIDModel"
        abstract = True
