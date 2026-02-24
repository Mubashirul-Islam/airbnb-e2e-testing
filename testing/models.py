from django.db import models

class Result(models.Model):
    test_id = models.CharField(max_length=100)
    test_case = models.CharField(max_length=255)
    url = models.URLField()
    passed = models.BooleanField()
    comment = models.TextField()
