from django.db import models
from web_server.models.Owner import Owner

class Whatever(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    is_auth = models.BooleanField(default=False)
