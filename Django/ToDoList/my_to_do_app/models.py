from django.db import models

# Create your models here.
class ToDo(models.Model):
    contents = models.CharField(max_length=255)  #한 줄이 컬럼이라고 생각하면 편할듯
    doDone = models.BooleanField(default=False)