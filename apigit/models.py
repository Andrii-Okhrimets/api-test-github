from django.db import models

class API_GIT(models.Model):
    login = models.CharField(max_length=100)

    def __str__(self):
        return self.login
