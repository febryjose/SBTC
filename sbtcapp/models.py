from django.db import models

class Gallery(models.Model):
    images = models.FileField(upload_to='uploads/')
    
    def __unicode__(self):
        return str(self.images)
