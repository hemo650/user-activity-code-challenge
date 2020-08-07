from django.db import models

# Create your models here.
class User(models.Model): 
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 25)
    last_login = models.DateTimeField()
    login_count = models.IntegerField()
    project_count = models.IntegerField()


