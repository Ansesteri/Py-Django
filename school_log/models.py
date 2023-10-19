from django.db import models

# Create your models here.
class SchoolMessage(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField(null=True, blank=True, verbose_name="Description")
   mark = models.IntegerField(null=True, blank=True)
   published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Date")
   subject = models.ForeignKey('Subject', null=True, on_delete=models.PROTECT, verbose_name="Subject")

   class Meta:
      verbose_name="School log"
      verbose_name_plural="School logs"
      ordering = ['-published']

class Subject(models.Model):
   name = models.CharField(max_length=30, db_index=True)

   def __str__(self):
      return self.name

   class Meta:
      ordering = ['name']