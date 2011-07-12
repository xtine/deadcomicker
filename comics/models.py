from django.db import models
import datetime

class Comic(models.Model):
    title = models.CharField(max_length=300)
    entry = models.TextField(blank=True)
    image = models.FileField(upload_to='comics', max_length=500, blank=True)
    created = models.DateField(editable=False)
    updated = models.DateTimeField(editable=False)
    
    def save(self):
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(Comic, self).save()
    
    def __unicode__(self):
        return self.title
    