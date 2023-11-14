from django.db import models

class VideoImportSettingsManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class VideoImportSettings(models.Model):
    name = models.CharField(max_length=255)
    processor = models.ForeignKey('EndoscopyProcessor', on_delete=models.CASCADE)
    center = models.ForeignKey('Center', on_delete=models.CASCADE)

    objects = VideoImportSettingsManager()

    def natural_key(self):
        return (self.name,)
    