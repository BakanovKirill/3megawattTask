from django.db import models


# Create your models here.
class Site(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Record(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='records')

    date_created = models.DateTimeField(auto_now_add=True)
    a_value = models.DecimalField(max_digits=6, decimal_places=2)
    b_value = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "%s: %s" % (self.site.title, self.date_created)
