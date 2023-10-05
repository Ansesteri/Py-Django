from django.db import models

# Create your models here.
class BoardMessage(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField(null=True, blank=True, verbose_name="Description")
   price = models.FloatField(null=True, blank=True)
   published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Date")

   class Meta:
      verbose_name="Board of announcements"
      verbose_name_plural="Board of announcements"
      ordering = ['-published']