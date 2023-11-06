from django.db import models


# not required to input date from Form, add "blank=True", if allow null, model add "null=True"
class Index(models.Model):
    key_words = models.CharField(max_length=2083, null=True)
    address = models.CharField(max_length=2083, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_click_date = models.DateTimeField(null=True)
    click_times = models.IntegerField(default=0, null=True)
