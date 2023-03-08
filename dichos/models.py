from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Dicho(models.Model):
    dichos_category = [
        (None, "Misc"),
        ("Life", "Life"),
        ("Patience", "Patience"),
        ("Motivation", "Motivation"),
        ("Gratitude", "Gratitude"),
        ("Relationships", "Relationships"),
        ("Love", "Love"),
        ("Funny", "Funny"),

    ]
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    saying = models.TextField(default='')
    translation = models.TextField(default='')
    category = models.CharField(choices=dichos_category, max_length=64)

    def __str__(self):
        return self.saying
