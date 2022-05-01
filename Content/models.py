from django.db import models

# Create your models here.
class Data(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    doc=models.FileField(upload_to="Content/docs")
    def __str__(self):
        return self.name