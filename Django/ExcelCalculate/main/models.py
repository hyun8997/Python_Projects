from django.db import models

# main models.py

class User(models.Model):
    user_name = models.CharField(max_length=20)  # 20자 제한
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)
    user_validate = models.BooleanField(default=False)


