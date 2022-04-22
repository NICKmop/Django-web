from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField(verbose_name='Site URL')
    
    def __str__(self):
        return '이름 : ' + self.site_name + ', 주소(URL) : ' + self.url