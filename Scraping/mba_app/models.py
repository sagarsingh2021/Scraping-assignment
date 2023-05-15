from django.db import models

# Create your models here.


from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    # description = models.TextField()
    # logo_url = models.URLField()
    website_url = models.URLField()
    location = models.CharField(max_length=255)
    scholarship = models.CharField(max_length=255)
    # country = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
