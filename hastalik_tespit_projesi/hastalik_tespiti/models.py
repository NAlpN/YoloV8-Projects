from django.db import models

class Hastalik(models.Model):
    ad = models.CharField(max_length=100)
    # Diğer alanlar buraya eklenecek

    def __str__(self):
        return self.ad
