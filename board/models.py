from django.db import models

# Create your models here.
class BoardMessage(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField(null=True, blank=True, verbose_name="Description")
   price = models.FloatField(null=True, blank=True)
   published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Date")
   rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name="Rubric")

   class Meta:
      verbose_name="Board of announcements"
      verbose_name_plural="Board of announcements"
      ordering = ['-published']


class Rubric(models.Model):
   name = models.CharField(max_length=30, db_index=True)

   def __str__(self):
      return self.name

   class Meta:
      ordering = ['name']