#db
from django.db import models

# Create your models here.
class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)