from django.db import models

from django.db import models
from django.utils import timezone
# Create your models here.

class Bookmark(models.Model):
    #id = models.AutoField(auto_created=True, primary_key=True, seriialize=False,)
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    date = models.DateTimeField('date',default=timezone.now, null = True, blank = True)

    def __str__(self):
        return self.title
        #return '%s %s' %(self.title, self.url)
# Create your models here.
