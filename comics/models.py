from django.db import models
from filebrowser.fields import FileBrowseField

class Comic(models.Model):
    title = models.CharField(max_length=300)
    entry = models.TextField(blank=True)
    # image = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True, null=True)
    image = models.FileField(upload_to='images', max_length=500)
    pub_date = models.DateTimeField('date published')
    